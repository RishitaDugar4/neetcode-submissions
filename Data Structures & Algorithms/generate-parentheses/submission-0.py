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

        def backtrack(opening, closing, stack):
            if opening == closing == n:
                result.append("".join(stack.copy()))
                return

            if opening < n:
                stack.append('(')
                backtrack(opening+1, closing, stack)
                stack.pop()

            if closing < opening:
                stack.append(')')
                backtrack(opening, closing+1, stack)
                stack.pop()
        
        backtrack(0, 0, [])
        return result
        