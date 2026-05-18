from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:        
        n = len(arr)
        graph = defaultdict(list)
        visited = set()
        visited.add(0)
        
        for i in range(n):
            graph[arr[i]].append(i)

        q = deque([0])
        jumps = 0

        while q:
            size = len(q)

            for _ in range(size):
                node = q.popleft()

                if node == n - 1:
                    return jumps
                
                for nei in graph[arr[node]]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
                
                graph[arr[node]].clear()
                left = node + 1
                right = node - 1

                if 0 <= left < n and left not in visited:
                    visited.add(left)
                    q.append(left)
                
                if 0 <= right < n and right not in visited:
                    visited.add(right)
                    q.append(right)
            
            jumps += 1

        return -1

def main():
    sol = Solution()
    print(sol.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
    print(sol.minJumps([7]))
    print(sol.minJumps([7,6,9,6,9,6,9,7]))

if __name__ == '__main__':
    main()