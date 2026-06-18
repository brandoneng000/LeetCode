from typing import List

class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        curr = [0] * n
        prev = [0] * n

        for day in range(k - 1, -1, -1):
            for city in range(n):
                move = max(map(sum, zip(prev, travelScore[city])))
                stay = max(curr[city], prev[city] + stayScore[day][city])

                curr[city] = max(move, stay)
            
            prev, curr = curr, prev
        
        return max(prev)
        
def main():
    sol = Solution()
    print(sol.maxScore(n = 2, k = 1, stayScore = [[2,3]], travelScore = [[0,2],[1,0]]))
    print(sol.maxScore(n = 3, k = 2, stayScore = [[3,4,2],[2,1,2]], travelScore = [[0,2,1],[2,0,4],[3,2,0]]))

if __name__ == '__main__':
    main()