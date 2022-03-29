class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        res = False
        for i in range(V):
            visited = [False]*V
            res = self.dfs(i, adj, visited)
            if res == True:
                break
            return res
            
    def dfs(self, v, adj, visited):
        if visited[v] == True:
	         return True
        else:
            neighbours = adj[v]
            if visited[v] == False:
                visited[v] = True
                for neighbour in neighbours:
                    if self.dfs(neighbour, adj, visited):
    	                    return True
                visited[v] = False
	        return False
