from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, jump = questions[i]
            dp[i] = max(points + dp[min(jump + i + 1, n)], dp[i + 1])
        
        return dp[0]
        
def main():
    sol = Solution()
    print(sol.mostPoints([[3,2],[4,3],[4,4],[2,5]]))
    print(sol.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))

if __name__ == '__main__':
    main()