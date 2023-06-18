import heapq
class ExamRoom:

    def __init__(self, n: int):
        self.size = n
        self.heap = [(self.dist(-1, n), -1, n)]

    def seat(self) -> int:
        _, x, y = heapq.heappop(self.heap)
        if x == -1:
            seat = 0
        elif y == self.size:
            seat = self.size - 1
        else:
            seat = (x + y) // 2
        heapq.heappush(self.heap, (self.dist(x, seat), x, seat))
        heapq.heappush(self.heap, (self.dist(seat, y), seat, y))
        return seat

    def leave(self, p: int) -> None:
        head = tail = None
        for interval in self.heap:
            if interval[1] == p:
                tail = interval
            if interval[2] == p:
                head = interval
            if head and tail:
                break
        
        self.heap.remove(head)
        self.heap.remove(tail)
        self.heap.append((self.dist(head[1], tail[2]), head[1], tail[2]))
        heapq.heapify(self.heap)
    
    def dist(self, x, y):
        if x == -1:
            return -y
        elif y == self.size:
            return -(self.size - 1 - x)
        else:
            return -(abs(x-y) // 2)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)