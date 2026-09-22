class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(parens, opening, closing):    
            if opening < closing or opening > n:
                return

            if len(parens) == 2*n:
                result.append(parens)
                return

            backtrack(parens + '(', opening+1, closing)
            backtrack(parens + ')', opening, closing+1)
            
        backtrack("(", 1, 0)
        return result