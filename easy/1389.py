from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for num, index in zip(nums, index):
            target.insert(index, num)

        return target

def main():
    sol = Solution()
    print(sol.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
    print(sol.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
    print(sol.createTargetArray(nums = [1], index = [0]))

if __name__ == '__main__':
    main()