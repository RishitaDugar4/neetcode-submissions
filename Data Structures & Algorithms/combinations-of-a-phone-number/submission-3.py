class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        if not digits:
            return []

        result = []
        def backtrack(index: int, currStr: str):
            if len(currStr) == len(digits):
                result.append(currStr)
                return

            for char in digiChars[digits[index]]:
                backtrack(index+1, currStr+char)


        backtrack(0, "")

        return result