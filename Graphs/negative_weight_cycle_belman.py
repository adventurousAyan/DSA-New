class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		
		dis = [float('inf')]*n
		dis[0] = 0
		for i in range(1,n):
		    for edge in edges:
		        u = edge[0]
		        v = edge[1]
		        wt = edge[2]
		        if dis[u] + wt < dis[v]:
		            dis[v] = dis[u] + wt
	    for edge in edges:
		        u = edge[0]
		        v = edge[1]
		        wt = edge[2]
		        if dis[u] + wt < dis[v]:
		            return 1
		return 0