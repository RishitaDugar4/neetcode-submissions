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

        value = self.mapping[key]

        left, right = 0, len(value)-1

        while left <= right:
            mid = (left + right) // 2
            if value[mid][1] <= timestamp:
                result = value[mid][0]
                left = mid + 1

            else:
                right = mid - 1

        return result

        
