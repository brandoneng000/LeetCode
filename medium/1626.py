from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        age_score = sorted(zip(ages, scores), reverse=True)
        dp = [0] * n
        print(age_score)
        for i in range(n):
            dp[i] = age_score[i][1]

            for j in range(i):
                if age_score[j][1] >= age_score[i][1]:
                    dp[i] = max(dp[i], dp[j] + age_score[i][1])
            
        return max(dp)
        
def main():
    sol = Solution()
    print(sol.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
    print(sol.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))
    print(sol.bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]))

if __name__ == '__main__':
    main()