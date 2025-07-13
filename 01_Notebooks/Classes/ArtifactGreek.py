from .Artifact import Artifact


class ArtifactGreek(Artifact):
    def __init__(
        self,
        department,
        accessionYear,
        objectName,
        title,
        culture: str,
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
        super().__init__(
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
        )

        assert "Greek" in self.culture.lower(), "Artifact is not Greek."

        self.tags.append("Ancient Greece")
        self.tagsWikidataURL.append("https://www.wikidata.org/wiki/Q11772")
