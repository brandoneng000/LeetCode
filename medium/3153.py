from typing import List

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        nums = [str(num) for num in nums]
        res = 0

        for i in range(len(nums[0])):
            count = [0] * 10

            for num in nums:
                count[int(num[i])] += 1
            
            total = sum(count)

            for j in range(10):
                res += count[j] * (total - count[j])
                total -= count[j]
        
        return res

        
def main():
    sol = Solution()
    print(sol.sumDigitDifferences([13,23,12]))
    print(sol.sumDigitDifferences([10,10,10,10]))
    print(sol.sumDigitDifferences([4154, 1234]))

if __name__ == '__main__':
    main()