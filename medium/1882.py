from typing import List
from collections import deque
from heapq import heappush, heappop

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free_servers = []
        busy_servers = []
        res = [-1] * len(tasks)
        cur_time = 0
        
        for i, weight in enumerate(servers):
            heappush(free_servers, (weight, i))

        for i, task in enumerate(tasks):
            while busy_servers and busy_servers[0][0] <= cur_time:
                cur_time, weight, index = heappop(busy_servers)
                heappush(free_servers, (weight, index))

            if not free_servers:
                cur_time, weight, index = heappop(busy_servers)
                heappush(free_servers, (weight, index))
            
            weight, index = heappop(free_servers)
            res[i] = index
            heappush(busy_servers, (cur_time + task, weight, index))
            
            if cur_time <= i:
                cur_time += 1

        return res
            
            
        
        
def main():
    sol = Solution()
    print(sol.assignTasks(servers = [3,3,2], tasks = [1,2,3,2,1,2]))
    print(sol.assignTasks(servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]))

if __name__ == '__main__':
    main()