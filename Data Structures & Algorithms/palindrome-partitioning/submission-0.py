class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(result, currSet, index):
            if index == len(s):
                result.append(currSet.copy())
                return

            for j in range(index, len(s)):
                if isPalindrome(index, j):
                    currSet.append(s[index: j+1])
                    backtrack(result, currSet, j+1)
                    currSet.pop()

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        backtrack(result, [], 0)
        return result
        