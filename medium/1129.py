from typing import List
import collections

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n
        RED, BLUE = 1, 2
        graph = collections.defaultdict(list)
        q = collections.deque([(0, 0)])
        
        for start, end in redEdges:
            graph[start].append((end, RED))
        
        for start, end in blueEdges:
            graph[start].append((end, BLUE))
        
        distance = 0

        while q:
            size = len(q)

            for _ in range(size):
                node, prev_color = q.popleft()
                
                if res[node] == -1:
                    res[node] = distance
                
                for i, (next_node, next_color) in enumerate(graph[node]):
                    if next_node == -1 or next_color == prev_color:
                        continue
                    q.append((next_node, next_color))
                    graph[node][i] = (-1, next_color)
            
            distance += 1
        
        return res

def main():
    sol = Solution()
    print(sol.shortestAlternatingPaths(n = 5, redEdges = [[0,1],[1,2],[2,3],[3,4]], blueEdges = [[1,2],[2,3],[3,1]]))
    print(sol.shortestAlternatingPaths(n = 3, redEdges = [[0,1],[1,2]], blueEdges = []))
    print(sol.shortestAlternatingPaths(n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]))

if __name__ == '__main__':
    main()