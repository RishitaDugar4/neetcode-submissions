class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = ""
        stack = []

        for char in path + "/":
            if char == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += char

        return "/" + "/".join(stack)