from typing import List
from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill_count = Counter(skill)
        equal_skill, r = divmod(sum(skill), n // 2)
        res = 0

        if r:
            return -1
        
        for num in skill_count:
            compliment = equal_skill - num
            if compliment == num:
                res += num * num * skill_count[num] // 2
            else:
                if skill_count[num] != skill_count[compliment]:
                    return -1
                res += num * compliment * skill_count[num]
            skill_count[compliment] = 0
            skill_count[num] = 0
        
        return res

        
def main():
    sol = Solution()
    print(sol.dividePlayers([3,2,5,1,3,4]))
    print(sol.dividePlayers([3,4]))
    print(sol.dividePlayers([1,1,2,3]))

if __name__ == '__main__':
    main()