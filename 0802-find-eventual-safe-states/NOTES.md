Use the same approach as cycle detection in a directed graph, if there is a cycle the node will NEVER be a safe node.
If there is a cycle mark the node in check array as 0 else mark it as 1. At the end, add all the non null items in the check array to safeNodes array and return that
Optionally, to save space use
`return [i for i in range(V) if check[i]]`
and remove the safeNodes part to save space
​