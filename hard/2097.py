from typing import List
from collections import defaultdict, deque

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        def visit(node):
            while graph[node]:
                next_node = graph[node].popleft()
                visit(next_node)
            res.append(node)

        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        res = []

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        start_node = -1

        for node in out_degree:
            if out_degree[node] == in_degree[node] + 1:
                start_node = node
                break
        
        if start_node == -1:
            start_node = pairs[0][0]
        
        visit(start_node)
        res.reverse()
        paired_res = [[res[i - 1], res[i]] for i in range(1, len(res))]

        return paired_res

        
def main():
    sol = Solution()
    print(sol.validArrangement([[5,1],[4,5],[11,9],[9,4]]))
    print(sol.validArrangement([[1,3],[3,2],[2,1]]))
    print(sol.validArrangement([[1,2],[2,1],[1,3]]))

if __name__ == '__main__':
    main()