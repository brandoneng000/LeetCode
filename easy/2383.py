from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res = sum(energy) - initialEnergy + 1 if sum(energy) - initialEnergy + 1 > 0 else 0

        for exp in experience:
            if exp >= initialExperience:
                res += exp - initialExperience + 1
                initialExperience += exp - initialExperience + 1
                
            initialExperience += exp
            
        return res


def main():
    sol = Solution()
    print(sol.minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]))
    print(sol.minNumberOfHours(initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]))
    print(sol.minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4], experience = [2,5]))

if __name__ == '__main__':
    main()