class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recurse(index):
            if index == len(nums):
                return [[]]

            result = []
            perms = recurse(index + 1)
            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[index])
                    result.append(pCopy)

            return result
        return recurse(0)
            

        