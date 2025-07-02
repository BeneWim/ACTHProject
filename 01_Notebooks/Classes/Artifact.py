class Artifact:
    def __init__(
        self,
        title,
        description,
    ):
        # Attributes are up to you — choose fields from the MET dataset that will support your research goals.
        # You should create subclasses of this for specific types of artifacts
        self.title = title
        self.description = description

    def to_rdf(self):
        # returns an rdflib.Graph representation of the object (simplistic, does not need to have all the attributes represented in RDF)
        pass

    def wikidata_enrich(self):
        # enriches artifact metadata by querying Wikidata with SPARQL
        pass

    def similar_artworks(self):
        # queries both Chicago API or Cleveland Museum API to look for similar artworks (maybe they share the creator, place of creation, date of creation – up to you)

        pass
