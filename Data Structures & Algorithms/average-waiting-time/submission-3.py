class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currentTime = customers[0][0]
        waitTime = 0.0

        for arrival, time in customers:
            if currentTime > arrival:
                waitTime += currentTime - arrival
            else:
                currentTime = arrival

            waitTime += time
            currentTime += time

        return float(waitTime / len(customers))
