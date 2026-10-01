from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        hashmap defaultdict
            src = dests
            if dest not list return -1
        queue up the dests 
        iterate thru them
        apend their dests
        += the cost, min() to keep only the cheapest
        '''
        flightMap = [[] for _ in range(n)]
        queue = deque()
        dist = [[float("inf")] * (k+5) for _ in range(n)]
        for source, dest, price in flights:
            flightMap[source].append((dest, price))
            #((1, 200)...)

        dist[src][0] = 0 #dist[city][stops] = bestCost
        minheap = [(0, src, -1)] #cost=0, node, stop=-1
        while len(minheap):
            c, node, stops = heapq.heappop(minheap)

            if dst == node:
                return c

            if stops == k or dist[node][stops+1] < c: 
                #beststop found so far
                continue

            for neighbor, cost in flightMap[node]:
                newC = c + cost
                nextStop = 1 + stops
                if dist[neighbor][nextStop+1] > newC:
                    dist[neighbor][nextStop + 1] = newC
                    heapq.heappush(minheap, (newC, neighbor, nextStop))

        return -1
