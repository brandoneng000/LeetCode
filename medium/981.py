import collections
import bisect
import heapq

class TimeMap:

    def __init__(self):
        self.timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.timestamps[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        index = bisect.bisect(self.timestamps[key], timestamp, key=lambda x: x[0])

        if index - 1 < 0:
            return ""

        return self.timestamps[key][index - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)