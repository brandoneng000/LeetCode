from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        start_time = set([float('inf')])
        processes = defaultdict(list)
        res = []

        for index, (start, time) in enumerate(tasks):
            processes[start].append((time, index))
            start_time.add(start)
        
        sorted_time = sorted(start_time)
        cur_time = 0

        for i in range(len(sorted_time)):
            cur_time = max(cur_time, sorted_time[i])
            for time, index in processes[sorted_time[i]]:
                heappush(heap, (time, index))
            
            while heap:
                if cur_time >= sorted_time[i + 1]:
                    break

                time, index = heappop(heap)
                cur_time += time
                res.append(index)
        
        return res
            

        
def main():
    sol = Solution()
    print(sol.getOrder([[1,2],[2,4],[3,2],[4,1]]))
    print(sol.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))

if __name__ == '__main__':
    main()