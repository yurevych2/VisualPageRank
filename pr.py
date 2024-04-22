import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.colors import Normalize, LinearSegmentedColormap
from matplotlib.cm import ScalarMappable
from data import round_1, round_2, round_3



# Converts a graph adjacency list to a stochastic matrix
def graph_to_stochastic_matrix(graph):
    nodes = list(graph.keys())
    node_index = {node: idx for idx, node in enumerate(nodes)}
    n = len(nodes)
    stochastic_matrix = np.zeros((n, n))
    for node, edges in graph.items():
        if edges:
            for edge in edges:
                stochastic_matrix[node_index[edge], node_index[node]] = 1.0 / len(edges)
        else:  # Handle dangling nodes by distributing value
            stochastic_matrix[:, node_index[node]] = 1.0 / n # All edges of the node = 1/n ~ probability to jump to any page
    return stochastic_matrix



def calculate_pagerank_with_linear_algebra(graph, damping_factor=0.85, tol=1.0e-6):
    """Calculates PageRank using linear algebra (matrix operations)."""
    S = graph_to_stochastic_matrix(graph)
    n = S.shape[0]
    E = np.ones((n, n)) / n
    G = damping_factor * S + ((1 - damping_factor) * E)
    
    # Initialize pagerank vector
    pagerank = np.ones(n) / n
    
    # Power iteration
    for _ in range(100):  # Hard-coded iteration limit to prevent infinite loops
        new_pagerank = G.dot(pagerank)
        # Check for convergence
        if np.linalg.norm(new_pagerank - pagerank) < tol:
            break
        pagerank = new_pagerank
    
    return {node: pagerank[i] for i, node in enumerate(graph)}



# -----------------------------------------------------------------------------
# Visualizing tool
# -----------------------------------------------------------------------------



def visualize_pagerank_color_by_size(graph, pagerank):
    # Create a networkx graph from the adjacency list
    G = nx.DiGraph()
    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge)

    # Calculate the size of each node proportional to its PageRank score
    max_pagerank = max(pagerank.values())
    node_sizes = [pagerank[node] / max_pagerank * 1000 for node in G.nodes()]

    # Create a custom color map from light green to yellow to orange to light red
    colors = ["lightgreen", "yellow", "orange", "lightcoral"]
    cmap_name = "custom_rainbow"
    custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors)
    
    # Create a normalized list of PageRank values for the color map
    # Scale data within a specified range — in this case, between the minimum
    # and maximum PageRank values,so they can be appropriately mapped to colors
    norm = Normalize(vmin=min(pagerank.values()), vmax=max_pagerank)
    # Handles the mapping of normalized numbers to colors
    mappable = ScalarMappable(norm=norm, cmap=custom_cmap)

    # Plot the graph
    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, k=0.5)  # Increases distance between nodes
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=[pagerank[node] for node in G], cmap=custom_cmap, edgecolors='black', alpha=0.9)
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='black', width=2)
    nx.draw_networkx_labels(G, pos, font_size=12)

    # Add a color bar
    plt.colorbar(mappable, shrink=0.5, aspect=5, label='PageRank')
    plt.title('PageRank Visualization')
    plt.margins(0.1)
    plt.axis('off')
    plt.tight_layout()  # Minimizes clipping of labels

    plt.show()



if __name__ == "__main__":
    
    graph = {
        'A': [],
        'B': ['A'],
        'C': ['A'],
        'D': ['A']
    }

    pagerank_scores = calculate_pagerank_with_linear_algebra(round_1)
    print(pagerank_scores)
    visualize_pagerank_color_by_size(round_1, pagerank_scores)

    pagerank_scores = calculate_pagerank_with_linear_algebra(round_2)
    print(pagerank_scores)
    visualize_pagerank_color_by_size(round_2, pagerank_scores)
    
    pagerank_scores = calculate_pagerank_with_linear_algebra(round_3)
    print(pagerank_scores)
    visualize_pagerank_color_by_size(round_3, pagerank_scores)
