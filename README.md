# ACTHProject
# Goal of the Project: <br>
We want to answer the question: Has the acquisition of artifacts at the MET changed over time in terms of their type, artist, culture, size and credit-line? <br>

# Division of group work: <br>
    Cleaning the Data - Ben <br>
    Creating Classes: <br>
      Artifact - Ben <br>
      Artist - Francesca <br>
      Collection - Moritz <br>
    Machine Learning:  <br>
     Image based - Ben <br>
     Text based -  Ben <br>
    Visualizations:  <br>
      Metadata form CSV - Ben <br>
      ML results - Ben <br>
      RDF graphs - Moritz <br>
      UML graph - Francesca <br>

# Reasoning
We decided to only use the data in the dataframe that was categorized under the department of "Greek and Roman Art". Only those attributes were included that had values within this department (e.g., the department dataset had no specified "location" data).

Each member of the group created one class for the project. For Artist and Artifact, two subclasses were defined to ensure a clearer structure.
The subclasses ArtifactGreek and ArtifactRoman were chosen because these were the two dominant cultures in the dataset.
Painters and potters were identifiable occupations in the display_name field of the Artist class. This made it easy to distinguish them from other data points.

In Collection, the classes Artist and Artifact are combined to enable a holistic analysis of the dataset by linking artists to their respective artifacts.

The utils.py module was created to visualize the RDF graph. Otherwise, the visualization method would have had to be repeated in each class, leading to duplicate code.

Implemented methods in classes: 
- to_rdf: We tried to use the CIDOC CRM ontology as extensively as possible, enriching it with additional well-known ontologies and applying custom ones in specific cases.
- wikidata_enrich: In the Artifact class, we queried Wikidata to add human-readable descriptions, making qualitative analysis possible. In Artist, we added the date_of_birth since this information was missing in the MET dataframe.
- similar_artworks: This method searches for artifacts from the same culture in the Cleveland and Chicago datasets, as we aimed to focus on artworks from Roman and Greek cultures.

Machine Learning techniques: 
To answer our research question on how the acquisition of artifacts at the MET has changed over time, we used both image-based and text-based machine learning approaches to enhance our analysis.

Image-based ML:
We extract all the images having a roman tag from the AIC API. We than cluster these images in order to find different clusters of objects. This is supposed to further enhance our analysis of this period, because we now have a knowledge of certain clusters of artifacts and can than use these results to see if some clusters were collected earlier or later. This can help us analyse if certain visual styles or object types were collected during different periods.

Text-based ML:
Since not every object from the ancient roman and greek period might be in the Depart for Roman And Greek Art, we use clustering on the Culture column to see, if we can identify a cluster correlating to this period. This could than be used to identify all objects belonging to this culture and period without having to rely on the department assosiation. 

We wanted to expand this analysis using the data from other museums as well, but since not all of them have the same columns, we had to rely on the title column, as this is a consistent field across all datasources. We used this field to see if naming conventions and collected artworks are different between museums by clustering the titles and comparing if some clusters only appear in certain museums. However we only used a limited dataset from each museum and this analysis therefore is probably highly biased by the reduced dataset. 

Visualizations: 
Metadata Visualizations:
To answear our initial research question we created several meta-analysis visualizations to explore how collecting practices have changed over time. For this we usually used the time when an artifact entered the museum as a core metric for analysis.

RDF Graphs
UML Diagram: Shows the relationships and connections between our classes, as well as the attributes and methods used in each.

# Used Datasets
Art institut of Chicago 
https://api.artic.edu/docs/#quick-start
Metropolitan Museum New York
https://github.com/metmuseum/openaccess
Cleveland Museum of Art
https://openaccess-api.clevelandart.org/