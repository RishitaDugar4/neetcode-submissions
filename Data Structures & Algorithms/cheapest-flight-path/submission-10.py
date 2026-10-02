class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        1. adj
        2. dist => []
        3. minheap
            - dijkstras
        '''
        adjlist = [[] for _ in range(n)]
        for source, dest, price in flights:
            adjlist[source].append((dest, price))
        
        dist = [[float('inf')] * (k+5) for _ in range(n)] 
        dist[src][0] = 0 #src to itself with 0 stops = 0

        minheap = [(0, src, -1)] #cost=0, source=src, k=0
        
        while len(minheap) > 0:
            cost, source, stops = heapq.heappop(minheap)
            
            if source == dst:
                return cost

            if k == stops or dist[source][stops+1] < cost:
                continue

            for neighbor, cst in adjlist[source]:
                new_stops = 1 + stops
                new_cost = cst + cost
                if dist[neighbor][new_stops + 1] > new_cost:
                    dist[neighbor][new_stops + 1] = new_cost
                    heapq.heappush(minheap, (new_cost, neighbor, new_stops))

        return -1
