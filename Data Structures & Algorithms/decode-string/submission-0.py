class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(index):
            result = ''
            k = 0

            while index < len(s):
                if s[index].isdigit():
                    k = k * 10 + int(s[index])
                    index += 1
                elif s[index] == '[':
                    next_index, decoded = dfs(index + 1)
                    result += k * decoded
                    k = 0
                    index = next_index
                elif s[index] == ']':
                    return index + 1, result
                else:
                    result += s[index]
                    index += 1

            return index, result

        return dfs(0)[1]