from typing import List
from heapq import heappush, heappop, heapify

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        m = len(meetings)
        meetings.sort()
        rooms = list(range(n))
        rooms_usage = [0] * n
        heap = []
        waiting = []
        index = 0

        heapify(rooms)

        while heap or index < m or waiting:
            if heap and index < m:
                cur_time = min(heap[0][0], meetings[index][0])
            elif heap:
                cur_time = heap[0][0]
            elif index < m:
                cur_time = meetings[index][0]
            
            while heap and heap[0][0] <= cur_time:
                time, r = heappop(heap)
                rooms_usage[r] += 1
                heappush(rooms, r)

            while waiting and rooms:
                _, dur = heappop(waiting)
                heappush(heap, (cur_time + dur, heappop(rooms)))
            
            while index < m and cur_time >= meetings[index][0]:
                if rooms:
                    heappush(heap, (cur_time + (meetings[index][1] - meetings[index][0]), heappop(rooms)))
                else:
                    heappush(waiting, (index, meetings[index][1] - meetings[index][0]))
                index += 1
        
        return max(range(n), key=lambda x: rooms_usage[x])
            
        
def main():
    sol = Solution()
    print(sol.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]))
    print(sol.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]))

if __name__ == '__main__':
    main()