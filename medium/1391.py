from typing import List
import collections

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def helper(i: int, j: int, move: tuple, visited = True):
            if (
                not (0 <= i < n and 0 <= j < m)
                or not(move in mapping[grid[i][j]]) 
                or (visited and i == 0 and j == 0) 
            ):
                return False
            
            if i == n - 1 and j == m - 1:
                return True
            
            next_move = mapping[grid[i][j]][move]
            di, dj = next_move

            return helper(i + di, j + dj, next_move)

        n, m = len(grid), len(grid[0])
        up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
        directions = [up, down, left, right]
        mapping = {
            1: { right: right, left: left },
            2: { up: up, down: down },
            3 : { right : down, up : left },
            4 : { up : right, left : down },
            5 : { right : up, down : left },
            6 : { down : right, left : up }
        }
        
        for dir in directions:
            if helper(0, 0, dir, visited=False):
                return True
        
        return False


    # def hasValidPath(self, grid: List[List[int]]) -> bool:
    #     m, n = len(grid), len(grid[0])
    #     directions = {1: [(0,-1),(0,1)],
    #                   2: [(-1,0),(1,0)],
    #                   3: [(0,-1),(1,0)],
    #                   4: [(0,1),(1,0)],
    #                   5: [(0,-1),(-1,0)],
    #                   6: [(0,1),(-1,0)]}
        
    #     goal = (m - 1, n - 1)
    #     q = collections.deque([(0, 0)])
    #     visited = set([(0, 0)])

    #     while q:
    #         cur_r, cur_c = q.popleft()

    #         if (cur_r, cur_c) == goal:
    #             return True
            
    #         for dr, dc in directions[grid[cur_r][cur_c]]:
    #             r, c = cur_r + dr, cur_c + dc

    #             if 0 <= r < m and 0 <= c < n and (r, c) not in visited and (-dr, -dc) in directions[grid[r][c]]:
    #                 q.append((r, c))
    #                 visited.add((r, c))

    #     return False
        

def main():
    sol = Solution()
    print(sol.hasValidPath([[2,4,3],[6,5,2]]))
    print(sol.hasValidPath([[1,2,1],[1,2,1]]))
    print(sol.hasValidPath([[1,1,2]]))

if __name__ == '__main__':
    main()