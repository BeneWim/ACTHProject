import networkx as nx
import matplotlib.pyplot as plt


def visualize_rdf_graph(rdf_graph):
    nx_graph = nx.DiGraph()

    for subj, pred, obj in rdf_graph:
        nx_graph.add_edge(str(subj), str(obj), label=str(pred))

    # Draw graph
    pos = nx.spring_layout(nx_graph, k=0.5)
    edge_labels = nx.get_edge_attributes(nx_graph, "label")

    plt.figure(figsize=(12, 8))
    nx.draw(
        nx_graph,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="lightblue",
        font_size=8,
        arrows=True,
    )
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, font_size=6)
    plt.title("RDF Graph Visualization")
    plt.show()
