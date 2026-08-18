class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}

        for c in s:
            if c not in chars:
                chars[c] = 0
            chars[c] += 1

        for c in t:
            if c not in chars:
                chars[c] = 0

            chars[c] -= 1

        for c in chars:
            if chars[c] != 0:
                return False

        return True