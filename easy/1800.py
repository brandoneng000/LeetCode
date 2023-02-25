from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        prev = 0
        cur_sum = 0

        for num in nums:
            if num > prev:
                cur_sum += num
                result = max(result, cur_sum)
            else:
                cur_sum = num
            prev = num

        return result


def main():
    sol = Solution()
    print(sol.maxAscendingSum([10,20,30,5,10,50]))
    print(sol.maxAscendingSum([10,20,30,40,50]))
    print(sol.maxAscendingSum([12,17,15,13,10,11,12]))
    print(sol.maxAscendingSum([12]))
    print(sol.maxAscendingSum([3,6,10,1,8,9,9,8,9]))
    print(sol.maxAscendingSum([3,6,10,1,8,9,9,8,9,1000]))

if __name__ == '__main__':
    main()