class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        n = 1 = ["()"]
        n = 2 = ["(())", "()()"]
        '''
        '''
        for each par:
            [ add to stack
            ] 
        '''
        result = []
        def backtrack(parenOptions, opening, closing, result):
            if opening < closing or opening > n:
                return # early exit condition

            if len(parenOptions) == 2*n:
                result.append(parenOptions)
                return

            backtrack(parenOptions + '(', opening+1, closing, result)
            backtrack(parenOptions + ')', opening, closing+1, result)
        
        backtrack("(", 1, 0, result)
        return result