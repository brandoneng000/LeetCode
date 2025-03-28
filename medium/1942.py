from typing import List
from heapq import heappush, heappop

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        order = sorted(range(len(times)), key=lambda x: times[x][0])
        seats_empty, seats_taken = list(range(len(times))), []

        for i in order:
            arrival, leave = times[i]

            while seats_taken and seats_taken[0][0] <= arrival:
                heappush(seats_empty, heappop(seats_taken)[1])
            
            seat = heappop(seats_empty)
            
            if i == targetFriend:
                return seat
        
            heappush(seats_taken, (leave, seat))

    # def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
    #     n = len(times)
    #     friends = sorted((times[i][0], times[i][1], i) for i in range(n))
    #     seats = [False] * n
    #     heap = []

    #     for arrival, leave, index in friends:
    #         while heap and heap[0][0] <= arrival:
    #             leaving, _, s = heappop(heap)
    #             seats[s] = False
            
    #         for i in range(n):
    #             if not seats[i]:
    #                 if index == targetFriend:
    #                     return i
                    
    #                 seats[i] = True
    #                 heappush(heap, (leave, index, i))
    #                 break
                

        
def main():
    sol = Solution()
    print(sol.smallestChair(times = [[1,4],[2,3],[4,6]], targetFriend = 1))
    print(sol.smallestChair(times = [[3,10],[1,5],[2,6]], targetFriend = 0))

if __name__ == '__main__':
    main()