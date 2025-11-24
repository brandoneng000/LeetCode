from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        cur = 0

        for bit in nums:
            cur = (cur * 2 + bit) % 5
            res.append(cur == 0)
        
        return res

    # def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
    #     value = 0

    #     for index in range(len(nums)):
    #         value <<= 1
    #         value |= nums[index]
    #         nums[index] = value % 5 == 0

    #     return nums
    
def main():
    sol = Solution()
    print(sol.prefixesDivBy5([0,1,1]))
    print(sol.prefixesDivBy5([1,1,1]))

if __name__ == '__main__':
    main()