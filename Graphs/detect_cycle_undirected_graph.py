class DetectCycleUndirected:
    
	def isCycle(self, V, adj):
		#Code here
		res = False
		for i in range(V):
		    visited = [False]*V
		    res = self.dfs(i, adj, visited, -1)
		    if res == True:
		        break
		return res
		
		
	def dfs(self, v, adj, visited, parent):

	    if visited[v] == True:
	         return True
		else:
	         neighbours = adj[v]
	         visited[v] = True
	         for neighbour in neighbours:
	            if neighbour != parent:
	                return self.dfs(neighbour, adj, visited, v)
             return False