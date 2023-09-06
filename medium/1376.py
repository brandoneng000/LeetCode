from typing import List
import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        company = collections.defaultdict(list)

        for index, m in enumerate(manager):
            company[m].append(index)

        def bfs(m: int):
            if not company[m]:
                return 0
            
            time = 0
            for e in company[m]:
                time = max(time, bfs(e))
            
            return informTime[m] + time

        return bfs(headID)

def main():
    sol = Solution()
    print(sol.numOfMinutes(n = 11, headID = 4, manager = [5,9,6,10,-1,8,9,1,9,3,4], informTime = [0,213,0,253,686,170,975,0,261,309,337]))
    print(sol.numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
    print(sol.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]))
    print(sol.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))

if __name__ == '__main__':
    main()