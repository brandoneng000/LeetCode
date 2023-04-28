from typing import List

# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         graph = { i:[] for i in range(n) }
#         heights = { i:[] for i in range(n) }
#         visited = set()
#         for i, j in edges:
#             graph[i].append(j)
#             graph[j].append(i)
        
#         for i in range(n):
#             heights[self.dfs(i, visited, n, graph)].append(i)
#             visited.clear()
        
#         for i in range(n):
#             if len(heights[i]) != 0:
#                 return heights[i]

#     def dfs(self, node: int, visited: set, size: int, graph: dict):
#         if len(visited) == size:
#             return 1
        
#         cur_height = -1
#         visited.add(node)
#         for child in graph[node]:
#             if child not in visited:
#                 cur_height = max(cur_height, self.dfs(child, visited, size, graph))
        
#         return cur_height + 1

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves



def main():
    sol = Solution()
    print(sol.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
    print(sol.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))

if __name__ == '__main__':
    main()