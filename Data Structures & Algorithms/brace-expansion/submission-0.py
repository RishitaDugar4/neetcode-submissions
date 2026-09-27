class Solution:
    def expand(self, s: str) -> List[str]:
        res = []
        prep = []
        i = 0
        while i < len(s): 
            if s[i] == '{':
                temp = i
                while s[i] != '}':
                    i += 1
                if len(s[temp+1:i]) == 1:
                    prep.append(s[temp+1:i])
                    i += 1
                    continue
                temp = s[temp+1:i].split(',')
                temp.sort()
                prep.append(temp)

            else: 
                prep.append(s[i])

            i += 1
        
        def dfs(remaining: list[str], word: str):
            if len(remaining) == 0:
                res.append(word)
                return word
            
            if len(remaining[0]) == 1: 
                return dfs(remaining[1:], word+remaining[0])
            
            for element in remaining[0]:
                dfs(remaining[1:], word+element)
                
        dfs(prep, "")
        return res
