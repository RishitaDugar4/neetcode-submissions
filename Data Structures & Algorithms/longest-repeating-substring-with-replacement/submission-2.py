class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        AAABABB
        char = a
        left => 0 => a
        right => 5 => b
        count = 4
        '''
        charSet = set(s)
        result = 0

        for char in charSet:
            l = count = 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1

                while (r-l+1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1

                result = max(result, r-l+1)

        return result