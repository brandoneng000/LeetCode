from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])
        time_map = {}

        for src, dst, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)
        
        def dfs(src, adj):
            if src in visit:
                return
            
            visit.add(src)
            secrets.add(src)

            for nei in adj[src]:
                dfs(nei, adj)
            

        for t in sorted(time_map.keys()):
            visit= set()

            for src in time_map[t]:
                if src in secrets:
                    dfs(src, time_map[t])

        return list(secrets)
        
        
def main():
    sol = Solution()
    print(sol.findAllPeople(n = 5, meetings = [[1,4,3],[0,4,3]], firstPerson = 3))
    print(sol.findAllPeople(n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1))
    print(sol.findAllPeople(n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3))
    print(sol.findAllPeople(n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1))

if __name__ == '__main__':
    main()