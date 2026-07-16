class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        result = ""
        
        while (word1 and word2):
            if index % 2 == 0:
                result += word1[0 : 1]
                word1 = word1[1 : ]

            else:
                result += word2[0 : 1]
                word2 = word2[1 : ]

            index += 1

        if word1:
            result += word1
        else:
            result += word2
        
        return result

        