# There is an undirected star graph consisting of n nodes labeled from 1 to n. 
# A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. 
# Return the center of the given star graph.

# Breakdown:

# 1. Create a list for creating a undirected graph
# 2. Connect the pairs from the given graph values
# 3. Find the center node by calculating the number of elements in the graph divided by the given pair

graph_pair = [[1,2],[5,1],[1,3],[1,4]]
def star_graph_center(graph_pair): # O(n)
    # Visualization:
        # Node 1 pairs with Node[2,5,3,4]
        # So it has 5 elements such as 1, 1->2, 1->5, 1->3 and 1->4
        for pairs in range(len(graph_pair)):
            print(graph_pair[pairs])
            

star_graph_center(graph_pair)