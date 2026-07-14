class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = high

        while (low <= high):
            k = (low + high) // 2
            totalHours = 0

            for pile in piles:
                totalHours += math.ceil(float(pile) / k)

            if totalHours > h:
                low = k+1
            else:
                result = k
                high = k-1

        return result
                