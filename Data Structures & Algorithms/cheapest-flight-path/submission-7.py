class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightMap = [[] for _ in range(n)]
        dist = [[float("inf")] * (k+2) for _ in range(n)]

        for s, d, c in flights:
            flightMap[s].append((d, c))

        dist[src][0] = 0 #cost from src w 0 stopsUsed = 0 
        minheap = [(0, src, -1)] #cost=0, node=src, stops=-1

        while len(minheap):
            cost, node, stops = heapq.heappop(minheap)
            if dst == node:
                return cost

            if stops == k or dist[node][stops+1] < cost:
                continue

            for neighbor, c in flightMap[node]:
                nextCost = c + cost
                nextStop = 1 + stops
                if dist[neighbor][nextStop + 1] > nextCost:
                    dist[neighbor][nextStop + 1] = nextCost # min
                    heapq.heappush(minheap, (nextCost, neighbor, nextStop))

        return -1
        
        