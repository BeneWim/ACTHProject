from .Artist import Artist


class ArtistPotter(Artist):  # creates a subclass in the class artist
    def __init__(
        self, display_name, nationality=None, wikidata_uri=None, date_of_birth=None
    ):  # defining the class and its parameters (parameters found in the MET dataset but also through enritchment)
        super().__init__(display_name, nationality, wikidata_uri, date_of_birth)

        if "potter" not in self.display_name.lower():
            raise ValueError("Artist is not a potter.")
