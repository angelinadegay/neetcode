class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_val = [value, timestamp]
        self.timeMap[key].append(new_val)
    

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        left = 0
        right = len(self.timeMap[key]) - 1
        checking = self.timeMap.get(key, [])

        while left <= right:
            mid = (left + right) // 2
            if checking[mid][1] == timestamp:
                return checking[mid][0]

            elif checking[mid][1] < timestamp:
                res = checking[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res



        
