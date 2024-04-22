# VisualPageRank
Page Rank extended with handling dangling nodes and a visualization tool.


- pr.py - our implementation of Page Rank with linear algebra with extensions that handle dangling nodes and visualize the results. There is also an example of usage;
- pr_iterative.py - our implementation of iterative Page Rank with an example of usage;
- pr_embedded.py - the file contains a function that converts graphs from dictionary representation to a list of edges as our implementation of Page Rank works with dictionaries and the function from NetworkX works with lists of edges. There is also an example of usage;
- test.py - code for testing our implementation in comparison with the Page Rank from NetworkX;
- benchmark.py - code for measuring the time efficiency of extended Page Rank with linear algebra, iterative Page Rank, and the algorithm from NetworkX;
- data.py - the data we collected during the tic-tac-toe tournament.


Pictures:
- performance_plot.png - results of the benchmark (random graphs with 50, 100, 150, 200, 250, 300, 350, 400 nodes, the minimal time during 50 iterations per certain size of a graph);
- round_1.png - the visualization of the first round of the tournament;
- round_2.png - the visualization of the second round of the tournament;
- round_3.png - the visualization of the third round of the tournament.
