class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        '''
        go thru edges, 

        '''
        weaker = set([v for u, v in edges])
        champs = [i for i in range(n) if i not in weaker]
        return champs[0] if len(champs) == 1 else -1
            

