from typing import List
import collections

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = collections.deque([[0]])
        res = []
        while q:
            path = q.popleft()

            for node in graph[path[-1]]:
                if node == len(graph) - 1:
                    res.append(path + [node])
                elif node not in path:
                    q.append(path + [node])
        
        return res
            

def main():
    sol = Solution()
    print(sol.allPathsSourceTarget([[1,2],[3],[3],[]]))
    print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))

if __name__ == '__main__':
    main()