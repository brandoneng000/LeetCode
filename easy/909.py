from typing import List
import collections

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        size = n * n
        need = { 1: 0 }
        bfs = collections.deque([1])

        while bfs:
            pos = bfs.popleft()
            
            for i in range(pos + 1, pos + 7):
                a, b = (i - 1) // n, (i - 1) % n
                next = board[~a][b if a % 2 == 0 else ~b]
                if next > 0:
                    i = next
                if i == size:
                    return need[pos] + 1
                if i not in need:
                    need[i] = need[pos] + 1
                    bfs.append(i)
            
        return -1


def main():
    sol = Solution()
    print(sol.snakesAndLadders([[1,1,-1],[1,1,2],[-1,1,1]]))
    print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,36,-1,-1,-1]]))
    print(sol.snakesAndLadders([[-1,1,2,3,4,5],[-1,-1,-1,-1,-1,6],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
    print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
    print(sol.snakesAndLadders([[-1,-1],[-1,3]]))

if __name__ == '__main__':
    main()