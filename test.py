import random
import networkx as nx
from pr import calculate_pagerank_with_linear_algebra
from pr_embedded import dict_to_edges_list

def generate_graph(size):
    graph = {}
    for i in range(size):
        node = i + 1
        possible_connections = list(range(1, size))
        num_connections = random.randint(1, len(possible_connections))
        connections = random.sample(possible_connections, num_connections)
        graph[node] = connections

    return graph

# Epsilon
epsilon = 0.001

# Range of graph sizes to test
# graph_sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
graph_sizes = [50, 100, 150, 200, 250, 300]

if __name__ == "__main__":
    
    mistakes = 0
    for size in graph_sizes:
        print(f"Processing size {size}.")
        
        graph = generate_graph(size)
        edges = dict_to_edges_list(graph)
        embedded_resut = list(set(nx.pagerank(edges, 0.85).values()))
        la_resut = list(set(calculate_pagerank_with_linear_algebra(graph).values()))

        embedded_resut.sort()
        la_resut.sort()

        for i in range(len(embedded_resut)):
            if (la_resut[i] < embedded_resut[i] - epsilon) or (la_resut[i] > embedded_resut[i] + epsilon):
                mistakes = mistakes + 1

    print(f"Number of mistakes: {mistakes}.")
