class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # min heap
        # adj list
        flightsMap = [[] for _ in range(n)]
        dist = [[float('inf')] * (k+2) for _ in range(n)]
        for source, destin, cost in flights:
            flightsMap[source].append([destin, cost])

        dist[src][0] = 0 #0 stops to get to itself
        #dist measures lowest cost
        #src taking 0 stops = 0
        minheap = [(0, src, -1)] #cost, src, stop

        while minheap:
            cst, node, stops = heapq.heappop(minheap)
            
            if node == dst:
                return cst

            if stops == k or dist[node][stops+1] < cst:
                continue

            for nei_dest, nei_cost in flightsMap[node]:
                new_cost = nei_cost + cst
                nextStops = stops+1
                if dist[nei_dest][nextStops+1] > new_cost:
                    dist[nei_dest][nextStops+1] = new_cost
                    heapq.heappush(minheap, (new_cost, nei_dest, nextStops))

        return -1

                

