class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            x = stones.pop()
            y = stones.pop()

            if x - y != 0:
                stones.append(abs(y - x))
                stones.sort()

        stones.append(0)
        return stones[0]