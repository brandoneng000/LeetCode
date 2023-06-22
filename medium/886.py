from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = { i: [] for i in range(1, n + 1) }

        for p, d in dislikes:
            graph[p].append(d)
            graph[d].append(p)

        colors = [-1] * (n + 1)

        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == colors[node]:
                    return False
                if colors[neighbor] == -1:
                    if not dfs(neighbor, 1 - color):
                        return False
            return True
        
        for i in range(1, n + 1):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
            
        return True

def main():
    sol = Solution()
    print(sol.possibleBipartition(n = 4, dislikes = [[1,2],[1,3],[2,4]]))
    print(sol.possibleBipartition(n = 3, dislikes = [[1,2],[1,3],[2,3]]))

if __name__ == '__main__':
    main()