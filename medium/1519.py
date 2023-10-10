from typing import List
import collections

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(root: int):
            total = collections.Counter(labels[root])
            
            for child in graph[root]:
                if child not in visited:
                    visited.add(child)
                    total += dfs(child)
            
            res[root] = total[labels[root]]
            return total

        graph = collections.defaultdict(set)
        visited = set([0])
        res = [0] * n

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        dfs(0)
        return res
        

        
def main():
    sol = Solution()
    print(sol.countSubTrees(n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"))
    print(sol.countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"))
    print(sol.countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"))
    print(sol.countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"))

if __name__ == '__main__':
    main()