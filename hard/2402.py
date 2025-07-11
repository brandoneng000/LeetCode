from typing import List
from heapq import heappush, heappop, heapify

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms, used_rooms = list(range(n)), []
        heapify(unused_rooms)
        meeting_count = [0] * n

        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            
            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, [end, room])
            else:
                room_avail_time, room = heappop(used_rooms)
                heappush(used_rooms, [room_avail_time + end - start, room])
            meeting_count[room] += 1
        
        return meeting_count.index(max(meeting_count))

    # def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
    #     room_avaiability_time = [0] * n
    #     meeting_count = [0] * n

    #     for start, end in sorted(meetings):
    #         min_room_avail_time = float('inf')
    #         min_avail_time_room = 0
    #         found_unused_room = False

    #         for i in range(n):
    #             if room_avaiability_time[i] <= start:
    #                 found_unused_room = True
    #                 meeting_count[i] += 1
    #                 room_avaiability_time[i] = end
    #                 break
    #             if min_room_avail_time > room_avaiability_time[i]:
    #                 min_room_avail_time = room_avaiability_time[i]
    #                 min_avail_time_room = i
            
    #         if not found_unused_room:
    #             room_avaiability_time[min_avail_time_room] += end - start
    #             meeting_count[min_avail_time_room] += 1
        
    #     return meeting_count.index(max(meeting_count))


    # def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
    #     m = len(meetings)
    #     meetings.sort()
    #     rooms = list(range(n))
    #     rooms_usage = [0] * n
    #     heap = []
    #     waiting = []
    #     index = 0

    #     heapify(rooms)

    #     while heap or index < m or waiting:
    #         if heap and index < m:
    #             cur_time = min(heap[0][0], meetings[index][0])
    #         elif heap:
    #             cur_time = heap[0][0]
    #         elif index < m:
    #             cur_time = meetings[index][0]
            
    #         while heap and heap[0][0] <= cur_time:
    #             time, r = heappop(heap)
    #             rooms_usage[r] += 1
    #             heappush(rooms, r)

    #         while waiting and rooms:
    #             _, dur = heappop(waiting)
    #             heappush(heap, (cur_time + dur, heappop(rooms)))
            
    #         while index < m and cur_time >= meetings[index][0]:
    #             if rooms:
    #                 heappush(heap, (cur_time + (meetings[index][1] - meetings[index][0]), heappop(rooms)))
    #             else:
    #                 heappush(waiting, (index, meetings[index][1] - meetings[index][0]))
    #             index += 1
        
    #     return max(range(n), key=lambda x: rooms_usage[x])
            
        
def main():
    sol = Solution()
    print(sol.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]))
    print(sol.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]))

if __name__ == '__main__':
    main()