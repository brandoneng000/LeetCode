from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = set(tuple(queen) for queen in queens)
        res = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        def helper(d_r: int, d_c: int):
            cur_r, cur_c = king[0], king[1]
            while 0 <= cur_r < 8 and 0 <= cur_c < 8:
                if (cur_r, cur_c) in queen_set:
                    res.append([cur_r, cur_c])
                    break
                cur_r += d_r
                cur_c += d_c

        for d_r, d_c in directions:
            helper(d_r, d_c)
        
        return res

def main():
    sol = Solution()
    print(sol.queensAttacktheKing(queens = [[2,0],[1,6],[3,4],[4,1]], king = [3,5]))
    print(sol.queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))
    print(sol.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))

if __name__ == '__main__':
    main()