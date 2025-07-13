from rdflib import Graph, Literal, RDF, URIRef, Namespace, RDFS
from rdflib.namespace import DC, FOAF, DCTERMS, XSD
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
import requests

CLEVELAND_URL = "https://openaccess-api.clevelandart.org/api/artworks/"
CHICAGO_URL = "https://api.artic.edu/api/v1/artworks/search"


class Artifact:
    def __init__(
        self,
        department,
        accessionYear,
        objectName,
        title,
        culture,
        period,
        medium,
        classification,
        creditLine,
        objectWikidataURL,
        tags,
        tagsAATURL,
        tagsWikidataURL,
        dimensions,
        cm_value,
    ):
        # Attributes are up to you — choose fields from the MET dataset that will support your research goals.
        # You should create subclasses of this for specific types of artifacts
        self.department = department
        self.accessionYear = pd.Timestamp(accessionYear).year
        self.objectName = objectName
        self.title = title
        self.culture = culture
        self.period = period
        self.medium = medium
        self.classification = classification
        self.creditLine = creditLine
        self.objectWikidataURL = objectWikidataURL
        self.tags = eval(tags)
        self.tagsAATURL = eval(tagsAATURL)
        self.tagsWikidataURL = eval(tagsWikidataURL)
        self.dimensions = dimensions
        self.cm_value = cm_value

        self.enriched_tags = []

    @classmethod
    def from_dataframe(cls, df, index):
        return cls(
            df.loc[index, "Department"],
            df.loc[index, "AccessionYear"],
            df.loc[index, "Object Name"],
            df.loc[index, "Title"],
            df.loc[index, "Culture"],
            df.loc[index, "Period"],
            df.loc[index, "Medium"],
            df.loc[index, "Classification"],
            df.loc[index, "Credit Line"],
            df.loc[index, "Object Wikidata URL"],
            df.loc[index, "Tags"],
            df.loc[index, "Tags AAT URL"],
            df.loc[index, "Tags Wikidata URL"],
            df.loc[index, "Dimensions"],
            df.loc[index, "cm_value"],
        )

    def to_rdf(self):
        # returns an rdflib.Graph representation of the object (simplistic, does not need to have all the attributes represented in RDF)
        CRM = Namespace("http://www.cidoc-crm.org/cidoc-crm/")
        DC = Namespace("http://purl.org/dc/elements/1.1/")
        EX = Namespace("http://w3id.org/example/")
        W3 = Namespace("https://w3id.org/i40/sto")

        g = Graph()
        g.bind("crm", CRM)
        g.bind("dc", DC)
        g.bind("ex", EX)
        g.bind("w3", W3)

        if self.objectWikidataURL is None:
            self.objectWikidataURL = (
                f"http://w3id.org/example/artifact/{self.title.replace(' ', '_')}"
            )
        artifact_uri = URIRef(self.objectWikidataURL)

        g.add((artifact_uri, RDF.type, CRM["E22_Man-Made_Object"]))
        g.add(
            (
                artifact_uri,
                CRM.P4_has_time_span,
                Literal(str(self.accessionYear), datatype=XSD.gYear),
            )
        )
        g.add((artifact_uri, DC.title, Literal(self.title)))
        g.add((artifact_uri, CRM.P45_consists_of, Literal(self.medium)))
        g.add((artifact_uri, CRM.P2_has_type, Literal(self.objectName)))
        g.add(
            (
                artifact_uri,
                CRM.P107i_is_current_or_former_member_of,
                Literal(self.department),
            )
        )

        if isinstance(self.tags, list):
            for tag in self.tags:
                g.add((artifact_uri, CRM.P2_has_type, Literal(tag)))

        if isinstance(self.tagsWikidataURL, list):
            for url in self.tagsWikidataURL:
                g.add((artifact_uri, W3.hasWikidataEntity, URIRef(url)))

        if self.enriched_tags:
            for url, value in self.enriched_tags:
                g.add((URIRef(url), RDFS.comment, Literal(value)))

        return g

    def print_rdf(self):
        graph = self.to_rdf()

        print(graph.serialize(format="turtle"))

    def wikidata_enrich(self):
        if not isinstance(self.tagsWikidataURL, list):
            print("tagsWikidataURL is not a list, skipping enrichment.")
            return

        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setReturnFormat(JSON)

        for uri in self.tagsWikidataURL:
            qid = uri.split("/")[-1]
            query = f"""
            SELECT ?label ?description WHERE {{
              wd:{qid} rdfs:label ?label .
              OPTIONAL {{ wd:{qid} schema:description ?description . }}
              FILTER (lang(?label) = "en")
              FILTER (lang(?description) = "en")
            }}
            LIMIT 1
            """
            try:
                sparql.setQuery(query)
                results = sparql.query().convert()
                for result in results["results"]["bindings"]:
                    label = result["label"]["value"]
                    description = result.get("description", {}).get("value", "")
                    self.enriched_tags.append((uri, description))
            except Exception as e:
                print(f"Error querying {qid}: {e}")

    def similar_artworks(self, limit: int = 5):
        # queries both Chicago API or Cleveland Museum API to look for similar artworks
        # (maybe they share the creator, place of creation, date of creation – up to you)

        if not self.classification:
            print("No classification available for this artifact.")
            return []

        results = self.similiar_artworks_chicago(limit)

        results = results + self.similiar_artworks_cleveland(limit)

        if not results:
            print("No similar artworks found in either collection.")

        return results

    def similiar_artworks_chicago(self, limit):
        # This uses full text search, which can be quiet broad,
        # because Chicago does not have a culture attribute

        results = []

        chicago_params = {
            "q": self.culture,
            "limit": limit,
            "fields": "id,title,date_display",
        }
        try:
            response = requests.get(CHICAGO_URL, params=chicago_params)
            response.raise_for_status()
            data = response.json()
            for item in data.get("data", []):
                results.append(
                    {
                        "source": "Chicago",
                        "title": item.get("title"),
                        "date": item.get("date_display", "Unknown"),
                        "url": f"https://www.artic.edu/artworks/{item['id']}",
                    }
                )
        except Exception as e:
            print(f"Error fetching from Chicago: {e}")

        return results

    def similiar_artworks_cleveland(self, limit):
        params = {"culture": self.culture, "limit": limit}

        try:
            response = requests.get(CLEVELAND_URL, params=params)
            response.raise_for_status()

            data = response.json()

            similar = []
            for result in data.get("data", []):
                similar.append(
                    {
                        "id": result.get("id"),
                        "title": result.get("title"),
                        "date": result.get("creation_date", "Unknown"),
                        "url": result.get("url"),
                    }
                )

            return similar

        except Exception as e:
            print(f"Error fetching similar artworks: {e}")
            return []
