from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        def dp():
            prev = [-float('inf')] * n
            curr = [-float('inf')] * n
            prev[n - 1] = fruits[0][n - 1]

            for i in range(1, n - 1):
                for j in range(max(n - 1 - i, i + 1), n):
                    best = prev[j]

                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    curr[j] = best + fruits[i][j]
                
                prev, curr = curr, prev
            
            return prev[n - 1]

        n = len(fruits)
        res = sum(fruits[i][i] for i in range(n))

        res += dp()
        
        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
        
        res += dp()
        return res
        
def main():
    sol = Solution()
    print(sol.maxCollectedFruits([[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]))
    print(sol.maxCollectedFruits([[1,1],[1,1]]))
    print(sol.maxCollectedFruits([[1,1],[1,1]]))

if __name__ == '__main__':
    main()