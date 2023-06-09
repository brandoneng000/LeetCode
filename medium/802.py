from typing import List
import collections

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        node_graph = { i:graph[i] for i in range(len(graph))}

        looped = set()
        visited = set()
        res = []

        def helper(node: int):
            if node in looped:
                return True
            if node in visited:
                return False
            visited.add(node)
            looped.add(node)
            for i in node_graph[node]:
                if helper(i):
                    return True

            looped.remove(node)
            return False

        for i in range(len(graph)):
            helper(i)

        for i in range(len(graph)):
            if i not in looped:
                res.append(i)

        return res

def main():
    sol = Solution()
    print(sol.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))
    print(sol.eventualSafeNodes(graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]))

if __name__ == '__main__':
    main()