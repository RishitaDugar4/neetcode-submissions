class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        charset = set(s)
        '''
        charset = set(s)
        result = 0

        for char in charset:
            count = l = 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1
                
                while (r-l+1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1

                result = max(result, r-l+1)

        return result