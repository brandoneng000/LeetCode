from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        right_odds = sum(nums[i] for i in range(1, n, 2))
        right_evens = sum(nums[i] for i in range(0, n, 2))
        left_odds = 0
        left_evens = 0

        for i in range(n):
            if i % 2 == 1:
                right_odds -= nums[i]
                if left_odds + right_evens == left_evens + right_odds:
                    res += 1
                left_odds += nums[i]
            else:
                right_evens -= nums[i]
                if left_odds + right_evens == left_evens + right_odds:
                    res += 1
                left_evens += nums[i]

        return res
        
def main():
    sol = Solution()
    print(sol.waysToMakeFair([2,1,6,4]))
    print(sol.waysToMakeFair([1,1,1]))
    print(sol.waysToMakeFair([1,2,3]))

if __name__ == '__main__':
    main()