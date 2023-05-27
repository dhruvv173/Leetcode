#Solution
from collections import deque
class Solution:
#Function to return Breadth First Traversal of given graph.
def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
    # code here
	vis = [0] * V
	vis[0] = 1
	q = deque()
	q.append(0)
	bfs = []    
	while q:
	  node = q.popleft()  # get the topmost element in the queue
    bfs.append(node)
    for it in adj[node]:  # traverse for all its neighbours
        if not vis[it]:  # if the neighbour has not been visited
            vis[it] = 1  # mark as visited
            q.append(it)  # store in the queue

    return bfs

#Problem link
# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1