from rdflib import Graph, Literal
from rdflib.namespace import RDF, RDFS, URIRef
from rdflib import Namespace
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON 
from .utils import visualize_rdf_graph

class Artist:
    def __init__(
        self, display_name, nationality=None, wikidata_uri=None, date_of_birth=None
    ):  # defining the class and its parameters (parameters found in the MET dataset but also through enritchment)
        self.display_name = (
            eval(display_name)[0] if isinstance(display_name, str) else "Unknown"
        )  # eval= parses string to python object
        self.nationality = nationality
        self.wikidata_uri = wikidata_uri
        self.date_of_birth = date_of_birth

    @classmethod
    def from_dataframe(
        cls, df: pd.DataFrame, index: int
    ):  # creates an artist from one row of the dataframe using the parameters defined above, by their index in the dataframe and the name of the column

        return cls(
            df.loc[index, "Artist Display Name"],
            df.loc[index, "Artist Nationality"],
            df.loc[index, "Artist Wikidata URL"],
        )

    def to_rdf(self):  # creates a rdf-graph for artist
        g = Graph()

        CRM = Namespace(
            "http://www.cidoc-crm.org/cidoc-crm/"
        )  # defining the ontologies
        DC = Namespace("http://purl.org/dc/elements/1.1/")
        EX = Namespace("http://w3id.org/example/")
        FOAF = Namespace("http://xmlns.com/foaf/0.1/")
        Schema = Namespace("http://schema.org/")

        g.bind(
            "crm", CRM
        )  # binding the abbreviation to the graph so when we serialize it, it will use #crm:something instead of the full namespace
        g.bind("dc", DC)
        g.bind("ex", EX)

        if self.wikidata_uri is None:
            self.wikidata_uri = f'http://w3id.org/example/artist/{self.display_name.replace(" ", "_")}'  # if there is no wikidata_uri in the dataframe, this line creates one out of the display_name. Spaces have to be replaced by _ to create a valid link.
        artist_uri = URIRef(
            self.wikidata_uri
        )  # creates a artist_uri out of the wikidata_uri

        g.add((artist_uri, RDF.type, CRM["E21_Person"])) #adds triples using the ontologies 
        g.add((artist_uri, FOAF.name, Literal(self.display_name)))
        g.add((artist_uri, Schema.nationality, Literal(self.nationality)))

        if self.date_of_birth:
            g.add(
                (artist_uri, Schema.birthDate, Literal(self.date_of_birth))
            )  # adds a birth date if there is one

        return g

    def print_rdf(self):  # prints the rdf graph in a turtle format
        graph = self.to_rdf()

        print(graph.serialize(format="turtle"))

    def wikidata_enrich(
        self,
    ):  # enriches the class information using a SPARQL querie to wikidata

        if not isinstance(
            self.wikidata_uri, str
        ):  # skips the enrichment if the data is not a string and prints an answer
            print("wikidata_uri is not a str, skipping enrichment.")
            return

        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setReturnFormat(JSON)

        qid = self.wikidata_uri.split("/")[-1]  # queries the optional birth date
        query = f"""
        SELECT ?date_of_birth WHERE {{
            OPTIONAL {{ wd:{qid} wdt:P569 ?date_of_birth . }}
            
        }}
        LIMIT 1
        """
        try:  # sends the query to wikidata to look if there is any infomation that was asked for
            sparql.setQuery(query)
            results = sparql.query().convert()
            for result in results["results"][
                "bindings"
            ]:  # if there is information it gets saved
                date_of_birth = result.get("date_of_birth", {}).get("value", "")
                self.date_of_birth = date_of_birth

        except Exception as e:
            print(f"Error querying {qid}: {e}") #prints a error if the query doesn't work

    def visualize_graph(self): #visualizes the rdf graph for artist 
        visualize_rdf_graph(self.to_rdf())