class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}':'{'}
        parens = []

        for char in s:
            if char in pairs:
                if not parens or parens.pop() != pairs[char]:
                    return False

            else:
                parens.append(char)

        return not parens
        