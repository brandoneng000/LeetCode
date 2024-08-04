from typing import List
from collections import Counter

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        count = Counter(nums)

        for move_from, move_to in zip(moveFrom, moveTo):
            if move_to == move_from:
                continue

            count[move_to] += count[move_from]
            count[move_from] -= count[move_from]
        
        return sorted(num for num in count if count[num] > 0)
        

def main():
    sol = Solution()
    print(sol.relocateMarbles(nums = [1,6,7,8], moveFrom = [1,7,2], moveTo = [2,9,5]))
    print(sol.relocateMarbles(nums = [1,1,3,3], moveFrom = [1,3], moveTo = [2,2]))

if __name__ == '__main__':
    main()