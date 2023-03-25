from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targets = {}

        for index, val in enumerate(nums):
            if val == key:
                if index + 1 < len(nums) and nums[index + 1] not in targets:
                    targets[nums[index + 1]] = 0
                if index + 1 < len(nums):    
                    targets[nums[index + 1]] += 1

        return max(targets, key=lambda x: targets[x])

def main():
    sol = Solution()
    print(sol.mostFrequent(nums = [1,100,200,1,100], key = 1))
    print(sol.mostFrequent(nums = [2,2,2,2,3], key = 2))
    print(sol.mostFrequent(nums = [11,22,11,33,11,33], key = 11))
    print(sol.mostFrequent(nums = [1,1], key = 1))

if __name__ == '__main__':
    main()