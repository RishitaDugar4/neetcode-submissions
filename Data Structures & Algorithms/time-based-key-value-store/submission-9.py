class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = []

        self.mapping[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        if key not in self.mapping:
            return result

        values = self.mapping[key]
        left, right = 0, len(values)-1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                left = mid + 1
                result = values[mid][0]

            else:
                right = mid - 1


        return result
        
