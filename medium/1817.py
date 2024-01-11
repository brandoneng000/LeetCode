from typing import List
from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        users = defaultdict(set)

        for id, time in logs:
            users[id].add(time)
        
        for id in users:
            res[len(users[id]) - 1] += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))
    print(sol.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4))

if __name__ == '__main__':
    main()