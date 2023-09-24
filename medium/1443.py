from typing import List
import collections

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node: int):
            if node in visited:
                return 0
            
            cur = 0
            visited.add(node)
            for n in graph[node]:
                cur += dfs(n)
            
            return cur + 2 if hasApple[node] or cur else cur
        
        graph = collections.defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        return max(dfs(0) - 2, 0)



def main():
    sol = Solution()
    print(sol.minTime(n = 4, edges = [[0,1],[1,2],[0,3]], hasApple = [True,True,True,True]))
    print(sol.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))
    print(sol.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))
    print(sol.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]))

if __name__ == '__main__':
    main()