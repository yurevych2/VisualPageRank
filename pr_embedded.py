import networkx as nx



def dict_to_edges_list(graph_adjacency):
    # Create a directed graph from the adjacency list
    G = nx.DiGraph()
    for node, edges in graph_adjacency.items():
        G.add_node(node)  # Ensure all nodes are added, even if they have no edges
        for edge in edges:
            G.add_edge(node, edge)
    
    return G



if __name__ == "__main__":

    graph = {
        'A': [],
        'B': ['A'],
        'C': ['A'],
        'D': ['A']
    }

    graph = dict_to_edges_list(graph)

    print(nx.pagerank(graph, alpha=0.85))
