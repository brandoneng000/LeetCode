from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        earnings = [0] * (max(nums) + 1)
        prev = curr = 0

        for earn in nums:
            earnings[earn] += earn
        
        for earn in earnings:
            prev, curr = curr, max(prev + earn, curr)
        return curr


def main():
    sol = Solution()
    print(sol.deleteAndEarn([8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]))
    print(sol.deleteAndEarn([3,4,2]))
    print(sol.deleteAndEarn([2,2,3,3,3,4]))

if __name__ == '__main__':
    main()