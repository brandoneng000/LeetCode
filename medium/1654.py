from typing import List
from heapq import heappop, heappush
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited = set([(0, False)])
        furthest = max([x] + forbidden) + a + b
        jumps = 0
        q = deque([(0, False)])

        for pos in forbidden:
            visited.add((pos, True))
            visited.add((pos, False))

        while q:
            size = len(q)

            for _ in range(size):
                node, back = q.popleft()

                if node == x:
                    return jumps
                
                forward, backward = (node + a, False), (node - b, True)

                if node + a <= furthest and forward not in visited:
                    visited.add(forward)
                    q.append(forward)
                
                if not back and node - b > 0 and backward not in visited:
                    visited.add(backward)
                    q.append(backward)
                
            jumps += 1
        
        return -1

    
def main():
    sol = Solution()
    print(sol.minimumJumps(forbidden = [18,13,3,9,8,14], a = 3, b = 8, x = 6))
    print(sol.minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9))
    print(sol.minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11))
    print(sol.minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7))

if __name__ == '__main__':
    main()