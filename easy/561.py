from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        
        for index in range(0, len(nums), 2):
            res += min(nums[index], nums[index + 1])

        return res


def main():
    sol = Solution()
    print(sol.arrayPairSum([1,4,3,2]))
    print(sol.arrayPairSum([6,2,6,5,1,2]))
    # 1 2 2 5 6 6

if __name__ == '__main__':
    main()