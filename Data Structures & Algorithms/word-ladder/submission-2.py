class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        transform beginword to any word within wordlist if
            - exactly one position the words have a different character
            - the rest of the positions have the same characters

        repeat with new word you need to obtain

        do until reach endword

        bfs
        - queue up all the values that are different by exactly 1 letter
            - 

        adjacency list

        '''
        if endWord not in wordList or beginWord == endWord:
            return 0

        count = 0
        words = set(wordList)
        queue = deque([beginWord])

        while queue:
            count += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count

                for i in range(len(word)):
                    for char in range(97, 123): #ascii
                        if chr(char) == word[i]:
                            continue
                        neighbor = word[:i] + chr(char) + word[i+1:]

                        if neighbor in words:
                            queue.append(neighbor)
                            words.remove(neighbor)
        return 0