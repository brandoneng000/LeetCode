from typing import List
import collections

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = {1: [(0,-1),(0,1)],
                      2: [(-1,0),(1,0)],
                      3: [(0,-1),(1,0)],
                      4: [(0,1),(1,0)],
                      5: [(0,-1),(-1,0)],
                      6: [(0,1),(-1,0)]}
        
        goal = (m - 1, n - 1)
        q = collections.deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            cur_r, cur_c = q.popleft()

            if (cur_r, cur_c) == goal:
                return True
            
            for dr, dc in directions[grid[cur_r][cur_c]]:
                r, c = cur_r + dr, cur_c + dc

                if 0 <= r < m and 0 <= c < n and (r, c) not in visited and (-dr, -dc) in directions[grid[r][c]]:
                    q.append((r, c))
                    visited.add((r, c))

        return False
        

def main():
    sol = Solution()
    print(sol.hasValidPath([[2,4,3],[6,5,2]]))
    print(sol.hasValidPath([[1,2,1],[1,2,1]]))
    print(sol.hasValidPath([[1,1,2]]))

if __name__ == '__main__':
    main()