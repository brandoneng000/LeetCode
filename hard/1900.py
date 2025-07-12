from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def dfs(n: int, p1: int, p2: int):
            if p1 + p2 == n + 1:
                return [1, 1]
            if p1 > p2:
                p1, p2 = p2, p1
            if n <= 4:
                return [2, 2]
            
            m = (n + 1) // 2
            min_res, max_res = float('inf'), -float('inf')

            if p1 - 1 > n - p2:
                temp = n + 1 - p1
                p1 = n + 1 - p2
                p2 = temp
            
            if p2 * 2 <= n + 1:
                a = p1 - 1
                b = p2 - p1 - 1

                for i in range(a + 1):
                    for j in range(b + 1):
                        r1, r2 = dfs(m, i + 1, i + j + 2)
                        min_res = min(min_res, r1 + 1)
                        max_res = max(max_res, r2 + 1)
            else:
                p4 = n + 1 - p2
                a = p1 - 1
                b = p4 - p1 - 1
                c = p2 - p4 - 1

                for i in range(a + 1):
                    for j in range(b + 1):
                        offset = i + j + 1 + (c + 1) // 2 + 1
                        r1, r2 = dfs(m, i + 1, offset)
                        min_res = min(min_res, r1 + 1)
                        max_res = max(max_res, r2 + 1)
            
            return [min_res, max_res]
        
        return dfs(n, firstPlayer, secondPlayer)
        
def main():
    sol = Solution()
    print(sol.earliestAndLatest(n = 11, firstPlayer = 2, secondPlayer = 4))
    print(sol.earliestAndLatest(n = 5, firstPlayer = 1, secondPlayer = 5))

if __name__ == '__main__':
    main()