class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        range = 1 to n
        k numbers -> size of subset
        '''
        subsets, currSet = [], []
        
        def helper(i, n, subsets, currSet):
            '''
            i = curr number
            '''
            if len(currSet) == k:
                subsets.append(currSet.copy())
                return 
            if i > n: #num out of range of n
                return

            for j in range(i, n+1):
                currSet.append(j)
                helper(j+1, n, subsets, currSet)
                currSet.pop()

        helper(1, n, subsets, currSet)
        return subsets