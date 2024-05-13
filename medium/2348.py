from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        res = 0

        for i in range(n):
            if not nums[i]:
                count += 1
            else:
                count = 0
            res += count

        return res 

    # def zeroFilledSubarray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     prefix = [0] * n

    #     for i in range(n):
    #         if nums[i] == 0:
    #             prefix[i] = prefix[i - 1] + 1
        
    #     return sum(prefix)

        
def main():
    sol = Solution()
    print(sol.zeroFilledSubarray([0,0,0,0,0]))
    print(sol.zeroFilledSubarray([1,3,0,0,2,0,0,4]))
    print(sol.zeroFilledSubarray([0,0,0,2,0,0]))
    print(sol.zeroFilledSubarray([2,10,2019]))

if __name__ == '__main__':
    main()