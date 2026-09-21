class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digiChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index:int, result, currStr):
            if len(currStr) == len(digits):
                result.append(currStr)
                return

            for char in digiChars[digits[index]]: #digits is a string, can index w/ i
                backtrack(index+1, result, currStr + char)

                
        backtrack(0, result, "")

        return result


        