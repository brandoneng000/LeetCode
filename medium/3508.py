from typing import List
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.router_set = set()
        self.router_q = deque()
        self.destinations = defaultdict(deque)
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        data = (source, destination, timestamp)

        if data in self.router_set:
            return False
        
        self.router_set.add(data)
        self.router_q.append(data)
        self.destinations[destination].append(timestamp)

        if len(self.router_q) > self.size:
            src, dest, time = self.router_q.popleft()
            self.router_set.remove((src, dest, time))
            self.destinations[dest].popleft()
        
        return True


    def forwardPacket(self) -> List[int]:
        if not self.router_q:
            return []

        data = self.router_q.popleft()
        self.router_set.remove(data)
        self.destinations[data[1]].popleft()

        return list(data)
        
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect_left(self.destinations[destination], startTime)
        right = bisect_right(self.destinations[destination], endTime)

        return right - left
        

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)