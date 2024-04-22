# Initializes the PageRank scores of a graph with equal values for each node.
def initialize_pagerank(graph):
    n = len(graph)
    return {node: 1.0 / n for node in graph}



# Calculates the PageRank of each node in the graph, properly handling dangling nodes.
def calculate_iterative_pagerank(graph, damping_factor=0.85, max_iterations=100, tol=1.0e-6):
    pagerank = initialize_pagerank(graph)
    num_nodes = len(graph)
    for _ in range(max_iterations):
        new_pagerank = {}
        dangling_sum = sum(pagerank[node] for node in graph if len(graph[node]) == 0) / num_nodes
        for node in graph:
            total_rank = 0.0
            for incoming_node, outgoing_links in graph.items():
                if node in outgoing_links:
                    total_rank += pagerank[incoming_node] / len(outgoing_links)
            new_pagerank[node] = ((1 - damping_factor) / num_nodes) + (damping_factor * (total_rank + dangling_sum))
        
        # Check for convergence
        if sum(abs(new_pagerank[node] - pagerank[node]) for node in pagerank) < tol:
            break
        pagerank = new_pagerank

    return pagerank

if __name__ == "__main__":

    graph = {
        'A': [],
        'B': ['A'],
        'C': ['A'],
        'D': ['A']
    }

    pagerank_scores = calculate_iterative_pagerank(graph)
    print(pagerank_scores)
