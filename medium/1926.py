from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1])])
        visited = set([(entrance[0], entrance[1])])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        steps = 1

        while q:
            size = len(q)

            for _ in range(size):
                cur_r, cur_c = q.popleft()

                for dr, dc in directions:
                    r = cur_r + dr
                    c = cur_c + dc

                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited and maze[r][c] == '.':
                        if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                            return steps
                        
                        visited.add((r, c))
                        q.append((r, c))
            
            steps += 1
        
        return -1


def main():
    sol = Solution()
    print(sol.nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))
    print(sol.nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))
    print(sol.nearestExit(maze = [[".","+"]], entrance = [0,0]))

if __name__ == '__main__':
    main()