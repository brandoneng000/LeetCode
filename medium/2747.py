from typing import List
from collections import Counter

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        query_index = sorted([q, i] for i, q in enumerate(queries))
        count = Counter()
        logs.sort(key=lambda x: x[1])
        i = j = used = 0
        res = [0] * len(queries)

        for time, index in query_index:
            while i < len(logs) and logs[i][1] <= time:
                count[logs[i][0]] += 1
                used += count[logs[i][0]] == 1
                i += 1
            
            while j < i and logs[j][1] < time - x:
                count[logs[j][0]] -= 1
                used -= count[logs[j][0]] == 0
                j += 1
            
            res[index] = n - used
        
        return res


                    
def main():
    sol = Solution()
    print(sol.countServers(n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]))
    print(sol.countServers(n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]))

if __name__ == '__main__':
    main()