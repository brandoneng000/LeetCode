from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        id = [[0] * n for _ in range(m)]
        sx = sy = 0
        cnt = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    id[i][j] = 1 << cnt
                    cnt += 1

        full = 1 << cnt
        best_energy = [
            [[-1 for _ in range(full)] for _ in range(n)] for _ in range(m)
        ]
        best_energy[sx][sy][0] = energy

        q = deque()
        q.append((sx, sy, 0, energy, 0))

        while q:
            x, y, mask, e, steps = q.popleft()

            if mask == full - 1:
                return steps

            if e == 0:
                continue

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n or classroom[nx][ny] == 'X':
                    continue

                ne = energy if classroom[nx][ny] == 'R' else e - 1
                nmask = mask | id[nx][ny]

                if ne > best_energy[nx][ny][nmask]:
                    best_energy[nx][ny][nmask] = ne
                    q.append((nx, ny, nmask, ne, steps + 1))

        return -1


def main():
    sol = Solution()
    print(sol.minMoves(classroom = ["S.", "XL"], energy = 2))
    print(sol.minMoves(classroom = ["LS", "RL"], energy = 4))
    print(sol.minMoves(classroom = ["L.S", "RXL"], energy = 3))

if __name__ == '__main__':
    main()