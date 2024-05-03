from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def check_str(spell: int, potions: List[int]):
            left, right = 0, m - 1

            while left <= right:
                middle = (left + right) // 2
                
                if potions[middle] * spell >= success:
                    right = middle - 1
                else:
                    left = middle + 1
            
            return left

        n = len(spells)
        m = len(potions)
        potions.sort()
        res = [0] * n

        for i in range(n):
            index = check_str(spells[i], potions)
            res[i] = m - index

        return res
        
def main():
    sol = Solution()
    print(sol.successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))
    print(sol.successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16))

if __name__ == '__main__':
    main()