class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        result = 0
        l = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l+= 1

            if s[r] not in chars:
                chars.add(s[r])

            result = max(result, r-l+1)
            
        return result