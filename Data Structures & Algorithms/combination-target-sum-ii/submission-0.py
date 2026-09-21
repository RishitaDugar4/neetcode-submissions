class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        candidates.sort()

        def helper(index, subsets, currSet, runningSum):
            if runningSum > target or index > len(candidates):
                return
            
            if runningSum == target:
                subsets.append(currSet.copy())
                return

            for j in range(index, len(candidates)):
                if j > index and candidates[j-1] == candidates[j]:
                    continue

                if runningSum + candidates[j] > target:
                    return

                currSet.append(candidates[j])
                helper(j+1, subsets, currSet, runningSum + candidates[j])
                currSet.pop()

        helper(0, subsets, [], 0)
        return subsets