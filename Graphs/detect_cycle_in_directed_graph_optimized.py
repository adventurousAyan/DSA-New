class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        res = False
        visited = [False]*V
        dfsVisited =  [False]*V
		for i in range(V):
		    if visited[i] == False:
		        res = self.dfs(i, adj, visited, dfsVisited)
    		    if res == True:
    		        break
		return res
		
		
	def dfs(self, v, adj, visited, dfsVisited):
	     if dfsVisited[v] == True and visited[v] == True:
	         return True
	     else:
	         neighbours = adj[v]
	         if visited[v] == False:
        	     visited[v] = True
        	     dfsVisited[v] = True
        	     for neighbour in neighbours:
        	         if self.dfs(neighbour, adj, visited, dfsVisited):
        	               return True
        	     dfsVisited[v] = False
	         return False