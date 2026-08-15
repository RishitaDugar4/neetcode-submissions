class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sizes, result = [], []

        for s in strs: 
            sizes.append(len(s))

        for sizes in sizes:
            result.append(str(sizes))
            result.append(',')
        result.append('#')
        result.extend(strs)

        print(result)

        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes, result, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for size in sizes:
            result.append(s[i:i + size])
            i += size
        
        return result
