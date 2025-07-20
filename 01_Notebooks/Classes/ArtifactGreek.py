from .Artifact import Artifact


class ArtifactGreek(Artifact):
    """
    A subclass of Artifact specifically for Greek artifacts.

    This class enforces that the `culture` attribute includes 'Greek' (case-insensitive),
    and enriches the artifact with a fixed tag and Wikidata URL for Ancient Greece.

    Inherits:
        Artifact: The base artifact class with metadata, RDF export, and enrichment functionality.
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
        Initialize a Greek artifact with all standard artifact metadata.

        Validates that the culture string contains 'Greek' and adds standardized
        enrichment data for Ancient Greece.

        Args:
            department (str): Department responsible for the artifact.
            accessionYear (int or str): Year of accession.
            objectName (str): The type or name of the object.
            title (str): The title of the artifact.
            culture (str): Cultural attribution (must include 'Greek').
            period (str): Historical period.
            medium (str): Materials used.
            classification (str): Classification of the object (e.g., sculpture).
            creditLine (str): Acknowledgment of donor or acquisition.
            objectWikidataURL (str): URL to the artifact’s Wikidata entry.
            tags (list or str): Tags describing the object.
            tagsAATURL (list or str): AAT (Getty Thesaurus) tag URLs.
            tagsWikidataURL (list or str): Wikidata tag URLs.
            dimensions (str): Physical dimensions.
            cm_value (float): Measured size in centimeters.

        Raises:
            AssertionError: If 'Greek' is not found in the culture string.
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

        assert "greek" in self.culture.lower(), "Artifact is not Greek."

        self.tags.append("Ancient Greece")
        self.tagsWikidataURL.append("https://www.wikidata.org/wiki/Q11772")
