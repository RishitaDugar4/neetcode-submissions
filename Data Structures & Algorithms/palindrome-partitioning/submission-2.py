class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(res, curr, index):
            if index == len(s):
                result.append(curr.copy())
                return

            for j in range(index, len(s)): #index is start
                if isPalindrome(index, j): #j is end of substring 
                    curr.append(s[index:j+1]) #include j
                    backtrack(res, curr, j+1) 
                    #j is new starting index, no revisting visted letters
                    curr.pop()

        def isPalindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -=1 
            return True

        backtrack(result, [], 0)

        return result
