class Solution:
    def isPrefixAndSuffix(self, str1, str2) -> bool:
        if str2.startswith(str1) and str2.endswith(str1):
            return True
        return False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                first = words[i]
                second = words[j]
                if self.isPrefixAndSuffix(first, second):
                    print('are you here?', first, second)
                    result += 1

        return result


