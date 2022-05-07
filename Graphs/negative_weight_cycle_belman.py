class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		
		dis = [float('inf')]*n
		dis[0] = 0
		# Relax it for n-1 times
		for i in range(1,n):
		    for edge in edges:
		        u = edge[0]
		        v = edge[1]
		        wt = edge[2]
		        if dis[u] + wt < dis[v]:
		            dis[v] = dis[u] + wt
		# If there is a cycle it will further reduce, so relax one more time
	    for edge in edges:
		        u = edge[0]
		        v = edge[1]
		        wt = edge[2]
		        if dis[u] + wt < dis[v]:
		            return 1
		return 0