from rdflib import Graph, Literal
from rdflib.namespace import RDF, RDFS, URIRef
from rdflib import Namespace
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON 

class Artist:
    def __init__(self, display_name, nationality=None, wikidata_uri=None):
        # Artist Represents a person who created one or more artifacts.
        # You choose what attributes to store (e.g., name, lifespan, nationality, movement), and how to structure artist-artifact relationships.
        # You can create subclasses of artists for specific types (i.e., human vs organization)

        self.display_name = eval(display_name)[0] if isinstance(display_name, str) else "Unknown" #eval= parses string to python object
        self.nationality = nationality
        self.wikidata_uri = wikidata_uri
        self.date_of_birth = None

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame, index: int):
        """
        Instantiate an Artifact from a row in a pandas DataFrame.

        Args:
            df (pd.DataFrame): DataFrame containing artifact metadata.
            index (int): Index of the row to convert.

        Returns:
            Artifact: An instance of the Artifact class.
        """
        return cls(
            df.loc[index, "Artist Display Name"],
            df.loc[index, "Artist Nationality"],
            df.loc[index, "Artist Wikidata URL"]
        )

    def to_rdf(self):
        # returns an rdflib.Graph representation of the artist (simplistic, does not have to have all the attributes represented in RDF, just a proof of concept)
        g = Graph()

        CRM = Namespace("http://www.cidoc-crm.org/cidoc-crm/") #creating a namespace object
        DC = Namespace("http://purl.org/dc/elements/1.1/")
        EX = Namespace("http://w3id.org/example/")
        FOAF = Namespace("http://xmlns.com/foaf/0.1/")
        Schema = Namespace("http://schema.org/")

        g.bind("crm", CRM) # binding it to the graph so when we serialize it, it will use #crm:something instead of the full namespace
        g.bind("dc", DC)
        g.bind("ex", EX)

        if self.wikidata_uri is None: 
            self.wikidata_uri = f'http://w3id.org/example/artist/{self.display_name.replace(" ", "_")}'
        artist_uri = URIRef(self.wikidata_uri)

        g.add((artist_uri, RDF.type, CRM["E20_Person"]))
        g.add((artist_uri, FOAF.name, Literal(self.display_name)))
        g.add((artist_uri, Schema.nationality, Literal(self.nationality)))
        
        if self.date_of_birth: 
            g.add((artist_uri, Schema.birthDate, Literal(self.date_of_birth)))
        
        
        return g
    
    def print_rdf(self):
        """
        Print the RDF serialization of the artifact in Turtle format.
   def     """
        graph = self.to_rdf()

        print(graph.serialize(format="turtle"))

    def wikidata_enrich(self):
        """
        Enrich tag information using SPARQL queries to Wikidata.

        Appends English descriptions of tag entities to the `enriched_tags` list.
        """
        if not isinstance(self.wikidata_uri, str):
            print("wikidata_uri is not a str, skipping enrichment.")
            return

        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setReturnFormat(JSON)

    
        qid = self.wikidata_uri.split("/")[-1]
        query = f"""
        SELECT ?date_of_birth WHERE {{
            OPTIONAL {{ wd:{qid} wdt:P569 ?date_of_birth . }}
            
        }}
        LIMIT 1
        """
        try:
            sparql.setQuery(query)
            results = sparql.query().convert()
            for result in results["results"]["bindings"]:
                date_of_birth = result.get("date_of_birth", {}).get("value", "")
                self.date_of_birth = date_of_birth
        except Exception as e:
            print(f"Error querying {qid}: {e}")

    