from queue import PriorityQueue
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        #print(adj)
        arr = [float('inf')]*V
        arr[S] = 0
        queue = PriorityQueue()
        queue.put((0, S))
        
        while not queue.empty():
            val = queue.get()
            neighbours = adj[val[1]]
            prevwt = val[0]
            for neighbor in neighbours:
                combWt = prevwt + neighbor[1]
                if combWt < arr[neighbor[0]]:
                    arr[neighbor[0]] = min(arr[neighbor[0]], combWt)
                    queue.put((combWt, neighbor[0]))
        return arr


