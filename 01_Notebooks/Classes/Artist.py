class Artist:
    def __init__(self, name, birth_year=None, death_year=None):
        # Artist Represents a person who created one or more artifacts.
        # You choose what attributes to store (e.g., name, lifespan, nationality, movement), and how to structure artist-artifact relationships.
        # You can create subclasses of artists for specific types (i.e., human vs organization)

        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def to_rdf(self):
        # returns an rdflib.Graph representation of the artist (simplistic, does not have to have all the attributes represented in RDF, just a proof of concept)
        pass

    def wikidata_enrichment(self):
        # queries wikidata to obtain more information about the artist
        pass
