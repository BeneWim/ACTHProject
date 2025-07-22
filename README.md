# ACTHProject
## Goal of the Project: <br>
We want to answer the question: Has the acquisition of artifacts at the MET changed over time in terms of their type, artist, culture, size and credit-line? <br>

## Division of group work: <br>
### Cleaning the Data: <br>
Ben <br>
### Creating Classes: <br>
  Artifact - Ben <br>
  Artist - Francesca <br>
  Collection - Moritz <br>
### Machine Learning:  <br>
 Image based - Ben <br>
 Text based -  Ben <br>
### Visualizations:  <br>
  Metadata form CSV - Ben <br>
  ML results - Ben <br>
  RDF graphs - Moritz <br>
  UML graph - Francesca <br>

## Reasoning
We decided to only use the data in the dataframe that was categorized under the department of "Greek and Roman Art". Only those attributes were included that had values within this department (e.g., the department dataset had no specified "location" data).

Each member of the group created one class for the project. For Artist and Artifact, two subclasses were defined to ensure a clearer structure.
The subclasses ArtifactGreek and ArtifactRoman were chosen because these were the two dominant cultures in the dataset.
Painters and potters were identifiable occupations in the display_name field of the Artist class. This made it easy to distinguish them from other data points.

In Collection, the classes Artist and Artifact are combined to enable a holistic analysis of the dataset by linking artists to their respective artifacts.

The utils.py module was created to visualize the RDF graph. Otherwise, the visualization method would have had to be repeated in each class, leading to duplicate code.

### Implemented methods in classes: 
- to_rdf: We tried to use the CIDOC CRM ontology as extensively as possible, enriching it with additional well-known ontologies and applying custom ones in specific cases.
- wikidata_enrich: In the Artifact class, we queried Wikidata to add human-readable descriptions, making qualitative analysis possible. In Artist, we added the date_of_birth since this information was missing in the MET dataframe.
- similar_artworks: This method searches for artifacts from the same culture in the Cleveland and Chicago datasets, as we aimed to focus on artworks from Roman and Greek cultures.

### Machine Learning Techniques:
To answer our research question on how the acquisition of artifacts at the MET has changed over time, we used both image-based and text-based machine learning approaches to enhance our analysis.

### Image-Based ML:
We extracted all images tagged as Roman from the AIC API. We then clustered these images to identify different groups of objects. This allows us to deepen our analysis of this period, as we now have knowledge of specific clusters of artifacts. We can use these results to examine whether certain clusters were collected earlier or later, helping us analyze whether specific visual styles or object types were acquired during different time periods.

### Text-Based ML:
Since not every object from the ancient Roman and Greek periods is necessarily listed in the Department of Greek and Roman Art, we applied clustering to the Culture column to see whether we could identify a cluster corresponding to this period. This can help us identify all objects belonging to this culture and time period without relying solely on departmental classification.

We aimed to expand this analysis using data from other museums as well. However, since not all institutions use the same metadata schema, we had to rely on the title column, which is a consistent field across all data sources. We used this field to explore whether naming conventions and collected artworks differ between museums by clustering titles and checking whether certain clusters appear only in specific institutions. Due to alimited datasets usage  from each museum, however, this analysis is likely biased and should be interpreted with caution.

## Visualizations:
### Metadata Visualizations:
To answer our initial research question, we created several meta-analytical visualizations to explore how collecting practices have changed over time. For this purpose, we typically used the year an artifact entered the museum as a core metric for analysis.

### RDF Graphs:
Shows an RDF graph that using the function to_rdf of the Collection Class for an predeterminant range. The input files are selected entries of our data were the creator/painter is also known.
The RDF outputs were saved in the folder 03_RDF_outputs

### UML Diagram: 
Shows the relationships and connections between our classes, as well as the attributes and methods used in each.

## Used Datasets
- Art institut of Chicago 
https://api.artic.edu/docs/#quick-start
- Metropolitan Museum New York
https://github.com/metmuseum/openaccess
- Cleveland Museum of Art
https://openaccess-api.clevelandart.org/
