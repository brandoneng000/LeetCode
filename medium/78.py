from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def combination(combo: List[int], cur_num: int, size: int):
            if len(combo) == size:
                result.append(combo.copy())
            
            for index in range(cur_num + 1, len(nums)):
                combo.append(nums[index])
                combination(combo, index, size)
                combo.pop()
        
        for size in range(len(nums) + 1):
            combination([], -1, size)
        
        return result

def main():
    sol = Solution()
    print(sol.subsets([1,2,3]))
    print(sol.subsets([0]))

if __name__ == '__main__':
    main()