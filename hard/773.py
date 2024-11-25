from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        s = ''.join(str(num) for row in board for num in row)
        visited = set([s])
        q = deque([(s, s.index('0'))])
        res = 0

        while q:
            for _ in range(len(q)):
                t, i = q.popleft()

                if t == '123450':
                    return res
                
                x, y = divmod(i, n)

                for r, c in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                    if 0 <= r < m and 0 <= c < n:
                        num_list = list(t)
                        num_list[i], num_list[r * n + c] = num_list[r * n + c], '0'
                        s = ''.join(num_list)

                        if s not in visited:
                            visited.add(s)
                            q.append((s, r * n + c))
            
            res += 1
        
        return -1
        

def main():
    sol = Solution()
    print(sol.slidingPuzzle([[1,2,3],[4,0,5]]))
    print(sol.slidingPuzzle([[1,2,3],[5,4,0]]))
    print(sol.slidingPuzzle([[4,1,2],[5,0,3]]))

if __name__ == '__main__':
    main()