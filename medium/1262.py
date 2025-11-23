from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        if total % 3 == 0:
            return total

        remainder_one = []
        remainder_two = []

        for num in nums:
            r = num % 3

            if r == 1:
                remainder_one.append(num)
                remainder_one.sort()
                remainder_one = remainder_one[:2]
            elif r == 2:
                remainder_two.append(num)
                remainder_two.sort()
                remainder_two = remainder_two[:2]

        if total % 3 == 1:
            sub1 = remainder_one[0] if len(remainder_one) >= 1 else float('inf')
            sub2 = sum(remainder_two) if len(remainder_two) >= 2 else float('inf')
        else:
            sub1 = sum(remainder_one) if len(remainder_one) >= 2 else float('inf')
            sub2 = remainder_two[0] if len(remainder_two) >= 1 else float('inf')

        res = total - min(sub1, sub2)

        return res if res != float('inf') else 0


    # def maxSumDivThree(self, nums: List[int]) -> int:
    #     dp = [0, 0, 0]
    #     for n in nums:
    #         for i in dp[:]:
    #             dp[(n + i) % 3] = max(dp[(i + n) % 3], i + n)
        
    #     return dp[0]


    # def maxSumDivThree(self, nums: List[int]) -> int:
    #     def helper(total: int, index: int):
    #         if total % 3 == 0:
    #             self.res = max(self.res, total)
            
    #         for i in range(index, len(nums)):
    #             total += nums[i]
    #             helper(total, i + 1)
    #             total -= nums[i]

    #     self.res = 0
    #     helper(0, 0)
    #     return self.res

def main():
    sol = Solution()
    print(sol.maxSumDivThree([3,6,5,1,8]))
    print(sol.maxSumDivThree([4]))
    print(sol.maxSumDivThree([1,2,3,4,4]))

if __name__ == '__main__':
    main()