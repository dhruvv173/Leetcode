#User function Template for python3

class Solution:
    def findOrder(self, alien_dict, N, K):
        # Initialize adjacency list
        adj = [[] for _ in range(K)]
    
        # Construct adjacency list based on word comparisons
        for i in range(N - 1):
            w1, w2 = alien_dict[i], alien_dict[i + 1]
            minLen = min(len(w1), len(w2))
    
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[ord(w1[j]) - ord('a')].append(ord(w2[j]) - ord('a'))
                    break
    
        # Call DFS-based topological sort
        topo = self.topoSortDFS(K, adj)
    
        # Convert indices back to characters and concatenate them
        result = ""
        for node in topo:
            result += chr(node + ord('a'))
    
        return result
    
    def topoSortDFS(self, numNodes, adj):
        def dfs(node, visited, stack):
            visited[node] = True
    
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, stack)
    
            stack.append(node)
    
        visited = [False] * numNodes
        stack = []
    
        for node in range(numNodes):
            if not visited[node]:
                dfs(node, visited, stack)
    
        stack.reverse()
        return stack


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends