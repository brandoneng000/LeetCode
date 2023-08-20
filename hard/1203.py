from typing import List
import collections

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topo_sort(graph, degree):
            visited = []
            stack = [node for node in range(len(graph)) if degree[node] == 0]
            while stack:
                cur = stack.pop()
                visited.append(cur)
                for neighbor in graph[cur]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 0:
                        stack.append(neighbor)
            
            return visited if len(visited) == len(graph) else []
        
        group_id = m

        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        item_graph = [[] for _ in range(n)]
        item_degree = [0] * n

        group_graph = [[] for _ in range(group_id)]
        group_degree = [0] * group_id

        for cur in range(n):
            for prev in beforeItems[cur]:
                item_graph[prev].append(cur)
                item_degree[cur] += 1

                if group[cur] != group[prev]:
                    group_graph[group[prev]].append(group[cur])
                    group_degree[group[cur]] += 1
        
        item_order = topo_sort(item_graph, item_degree)
        group_order = topo_sort(group_graph, group_degree)

        if not item_order or not group_order:
            return []
        
        ordered_groups = collections.defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)
        
        res = []
        for group_index in group_order:
            res += ordered_groups[group_index]
        
        return res

def main():
    sol = Solution()
    print(sol.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]))
    print(sol.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]))

if __name__ == '__main__':
    main()