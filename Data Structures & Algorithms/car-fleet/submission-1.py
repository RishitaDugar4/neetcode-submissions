class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        result = []

        for p, s in cars:
            time = (target-p) / s
            result.append(time)

            if len(result) >= 2 and result[-1] <= result[-2]:
                result.pop()

        return len(result)


