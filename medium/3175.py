from typing import List

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        win_streak = 0
        res = 0
        cur_skill = skills[0]

        for i in range(1, n):
            if cur_skill > skills[i]:
                win_streak += 1
            else:
                win_streak = 1
                res = i
                cur_skill = skills[i]
            
            if win_streak >= k:
                break
        
        return res


        
def main():
    sol = Solution()
    print(sol.findWinningPlayer(skills = [4,2,6,3,9], k = 2))
    print(sol.findWinningPlayer(skills = [2,5,4], k = 3))

if __name__ == '__main__':
    main()