from .Artifact import Artifact


class ArtifactRoman(Artifact):
    """
    A subclass of Artifact specifically for Roman artifacts.

    This class ensures that the `culture` attribute includes 'Roman' (case-insensitive),
    and automatically enriches the artifact with a standardized tag and Wikidata URL
    representing the Roman Empire.

    Inherits:
        Artifact: The base artifact class with metadata handling, RDF export,
        tag enrichment, and API search for similar artifacts.
    """

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
        """
        Initialize a Roman artifact, validating cultural attribution and appending Roman-specific tags.

        Args:
            department (str): Department responsible for the artifact.
            accessionYear (int or str): Year of accession.
            objectName (str): The type or name of the object.
            title (str): The title of the artifact.
            culture (str): Cultural attribution (must include 'Roman').
            period (str): Historical period.
            medium (str): Materials used in the artifact.
            classification (str): Classification category of the object.
            creditLine (str): Donor or acquisition credit information.
            objectWikidataURL (str): URL to the artifact’s Wikidata entity.
            tags (list or str): Descriptive tags for the object.
            tagsAATURL (list or str): AAT (Getty) tag URLs.
            tagsWikidataURL (list or str): Wikidata tag URLs.
            dimensions (str): Dimensions of the artifact.
            cm_value (float): Physical measurement in centimeters.

        Raises:
            AssertionError: If 'Roman' is not found in the culture string.
        """
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
