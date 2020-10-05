# interestingLC
personal (optimized) solutions for interesting LeetCode problems based on basic understandings below.

Computer algorithms typically involve "exhaustive search" over the solution space,
no matter if the solution space a linear array or list, or a tree or a graph, using the following traversal methods.

For linear structures, we can use linear search, sliding window, two pointers; 
if ordered, then we can use bisecting method to achieve O(logN)

For tree structures, breadth first search (BFS) and depth first search (DFS) are needed.
For binary tree, BFS has preorder, in-order, post-order. 

For graphs, BFS and DFS are needed to traverse, with the attention to track if a vertex is visited or not in case loops exist. 
To check if a vertex is connected with a graph, disjoint set method will be handy.
To build a minimal spanning tree, Prim's BFS method or Kruskal's disjoint set method are studied.
Shortest path algorithm is BFS and is similar to Prim's algorithm.
Max flow algorithm is to be studied... 

Dictionary is magical extension to allow "any hashable stuff" to be the index. 
The effectiveness of hashing is given, but is not obvious if thinking from scratch.
A recursive dictionary is a trie.

Exhaustive method, albeit very useful, does not sound smart enough.
Greedy method is smart and can avoid exhaustive search of the solution space.
But greedy method requires methematical proof and is not straightforward to come up with. 
Typically, sorting is involved to establish convenience for "loop invariant". 
For example, if intervals are involved, then sorting by the starting point or ending point is typically needed. 
Proof typically involves establishing the proposed optimal solution as one solution; 
then prove that if it is not optimal, some contradiction will happen.

