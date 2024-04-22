import time
import random
import networkx as nx
import matplotlib.pyplot as plt
from pr import calculate_pagerank_with_linear_algebra
from pr_embedded import dict_to_edges_list
from pr_iterative import calculate_iterative_pagerank

def generate_graph(size):
    graph = {}
    for i in range(size):
        node = i + 1
        possible_connections = list(range(1, size))
        num_connections = random.randint(1, len(possible_connections))
        connections = random.sample(possible_connections, num_connections)
        graph[node] = connections

    return graph



# Measure the execution time of a function on a given graph
def measure_execution_time(func, arguments):
    if not arguments[1]:
        start_time = time.time()
        func(arguments[0])
        end_time = time.time()
    else:
        start_time = time.time()
        func(arguments[0], arguments[1])
        end_time = time.time()

    return end_time - start_time




# Range of graph sizes to test
graph_sizes = [50, 100, 150, 200, 250, 300, 350, 400]

num_iterations = 50

if __name__ == "__main__":
    execution_times_pr = []
    execution_times_embedded = []
    execution_times_iterative = []

    for size in graph_sizes:
        graph = generate_graph(size)
        edges = dict_to_edges_list(graph)
        print(f"Processing size {size}.")

        min_time = float("inf")
        for _ in range(num_iterations):
            min_time = min(min_time, measure_execution_time(calculate_pagerank_with_linear_algebra, (graph, 0)) * 1000)
        execution_times_pr.append(min_time)

        min_time = float("inf")
        for _ in range(num_iterations):
            min_time = min(min_time, measure_execution_time(nx.pagerank, (edges, 0.85)) * 1000)
        execution_times_embedded.append(min_time)

        min_time = float("inf")
        for _ in range(num_iterations):
            min_time = min(min_time, measure_execution_time(calculate_iterative_pagerank, (graph, 0)) * 1000)
        execution_times_iterative.append(min_time)

    plt.plot(graph_sizes, execution_times_pr, label='PR Function with Linear Algebra')
    plt.plot(graph_sizes, execution_times_embedded, label='NetworkX PR Function')
    plt.plot(graph_sizes, execution_times_iterative, label='Iterative PR Function')

    plt.xlabel('Graph Size (nodes)') 
    plt.ylabel('Execution Time (ms)')
    plt.title('Execution Time vs. Graph Size')
    plt.legend()

    plt.savefig('performance_plot.png')  # Save the plot as a PNG file
    plt.show()
