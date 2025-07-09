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
        self.accessionYear = accessionYear
        self.objectName = objectName
        self.title = title
        self.culture = culture
        self.period = period
        self.medium = medium
        self.classification = classification
        self.creditLine = creditLine
        self.objectWikidataURL = objectWikidataURL
        self.tags = tags
        self.tagsAATURL = tagsAATURL
        self.tagsWikidataURL = tagsWikidataURL
        self.dimensions = dimensions
        self.cm_value = cm_value

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
        pass

    def wikidata_enrich(self):
        # enriches artifact metadata by querying Wikidata with SPARQL
        pass

    def similar_artworks(self):
        # queries both Chicago API or Cleveland Museum API to look for similar artworks (maybe they share the creator, place of creation, date of creation – up to you)

        pass
