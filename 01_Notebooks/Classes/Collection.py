from Artifact import Artifact
from Artist import Artist


class Collection:
    def __init__(self, name):
        self.name = name

        self.artists = []  # List of Artist objects
        self.artifacts = []  # List of Artifact objects

    def add_artifact(self, artifact: Artifact):
        if not isinstance(artifact, Artifact):
            raise TypeError("Expected an instance of Artifact")

        self.artifacts.append(artifact)

    def add_artist(self, artist: Artist):
        if not isinstance(artist, Artist):
            raise TypeError("Expected an instance of Artist")

        self.artists.append(artist)

    def to_rdf(self):
        # returns an rdflib.Graph with all RDF triples from the collection –
        # artifacts and their creators must be linked!
        # **Not every single attribute needs to be represented in RDF, keep it simple as a proof of concept**

        pass

    def visualize_metadata(self):
        # generates visualizations from the raw dataset (e.g. pie charts, bar charts) up to you which ones

        pass

    def visualize_rdf(self):
        # generates RDF visualizations

        pass

    def cross_api_enrich(self):
        # finds additional works by the artists in the collection from the AIC or Cleveland API,
        # adds the items to the collection (with the metadata that they have from the APIs,
        # so you should consider about their metadata as well when you create attributes.
        # Remember you can put default attributes as None for things that are not shared between the APIs

        pass
