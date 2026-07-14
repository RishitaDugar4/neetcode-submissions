class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        result = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / mid)

            if hours > h:
                lo = mid + 1
            else:
                result = mid
                hi = mid - 1

        return result


        