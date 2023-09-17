from typing import List
import collections

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_mask = (1 << n) - 1
        visited = set()
        Node = collections.namedtuple('Node', ['node', 'mask', 'cost'])
        q = collections.deque([])

        for i in range(n):
            mask_val = (1 << i)
            n = Node(i, mask_val, 1)
            q.append(n)
            visited.add((i, mask_val))
        
        while q:
            cur = q.popleft()

            if cur.mask == all_mask:
                return cur.cost - 1
        
            for adj in graph[cur.node]:
                both_mask = cur.mask | (1 << adj)
                n = Node(adj, both_mask, cur.cost + 1)

                if (adj, both_mask) not in visited:
                    visited.add((adj, both_mask))
                    q.append(n)
        
        return -1

def main():
    sol = Solution()
    print(sol.shortestPathLength([[1,2,3],[0],[0],[0]]))
    print(sol.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))

if __name__ == '__main__':
    main()