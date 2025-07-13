from .Artifact import Artifact


class ArtifactRoman(Artifact):
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

        assert "roman" in self.culture.lower(), "Artifact is not Roman."

        self.tags.append("Roman Empire")
        self.tagsWikidataURL.append("https://www.wikidata.org/wiki/Q2277")
