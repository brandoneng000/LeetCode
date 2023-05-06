from typing import List
import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = collections.defaultdict(dict)
        res = []
        for (x, y), val in zip(equations, values):
            self.graph[x][y] = val
            self.graph[y][x] = 1 / val
        
        for x, y in queries:
            res.append(self.dfs(x, y, set()))

        return res
    
    def dfs(self, x, y, visited: set):
        if x not in self.graph or y not in self.graph:
            return -1.0
        
        if y in self.graph[x]:
            return self.graph[x][y]
        
        for i in self.graph[x]:
            if i not in visited:
                visited.add(i)
                temp = self.dfs(i, y, visited)
                if temp != -1:
                    return self.graph[x][i] * temp
        
        return -1


def main():
    sol = Solution()
    print(sol.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    print(sol.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(sol.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))

if __name__ == '__main__':
    main()