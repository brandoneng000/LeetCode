from typing import List
from collections import Counter

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def check_prime(num: int):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            
            return True

        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        count = Counter({-1: -1})

        for i in range(m):
            for j in range(n):
                
                for dr, dc in directions:
                    r, c = i, j
                    cur = mat[i][j]

                    while 0 <= r + dr < m and 0 <= c + dc < n:
                        r += dr
                        c += dc
                        cur = (cur * 10) + mat[r][c]

                        if cur in count:
                            count[cur] += 1
                        elif check_prime(cur) and cur > 10:
                            count[cur] += 1
        
        return max(count, key=lambda x: (count[x], x))
                    
        
def main():
    sol = Solution()
    print(sol.mostFrequentPrime([[1,2,6],[7,9,8]]))
    print(sol.mostFrequentPrime([[1,1],[9,9],[1,1]]))
    print(sol.mostFrequentPrime([[7]]))
    print(sol.mostFrequentPrime([[9,7,8],[4,6,5],[2,8,6]]))

if __name__ == '__main__':
    main()