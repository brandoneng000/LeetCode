from typing import List
from collections import defaultdict, Counter

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def dfs(node: int, graph: defaultdict, visited: List[int], count: List[List[int]], colors: str):
            if visited[node] == 1:
                return float('inf')
            
            if visited[node] == 2:
                return count[node][ord(colors[node]) - ord('a')]
            
            visited[node] = 1

            for nei in graph[node]:
                cur = dfs(nei, graph, visited, count, colors)

                if cur == float('inf'):
                    return float('inf')
                
                for c in range(26):
                    count[node][c] = max(count[node][c], count[nei][c])
            
            col = ord(colors[node]) - ord('a')
            count[node][col] += 1
            visited[node] = 2

            return count[node][col]
            

        n = len(colors)
        graph = defaultdict(list)
        count = [[0] * 26 for _ in range(n)]
        visited = [0] * n
        res = 0

        for a, b in edges:
            graph[a].append(b)

        for root in range(n):
            cur = dfs(root, graph, visited, count, colors)

            if cur == float('inf'):
                return -1
            
            res = max(res, cur)
        
        return res

def main():
    sol = Solution()
    print(sol.largestPathValue(colors = "hhqhuqhqff", edges = [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]))
    print(sol.largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]))
    print(sol.largestPathValue(colors = "a", edges = [[0,0]]))

if __name__ == '__main__':
    main()