from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prev = -100000

        for i in range(n):
            if nums[i]:
                if i - prev <= k:
                    return False
                prev = i
        
        return True

    # def kLengthApart(self, nums: List[int], k: int) -> bool:
    #     count = 0

    #     for num in nums:
    #         if count <= 0 and num == 1:
    #             count = k
    #         elif num == 1:
    #             return False
    #         else:
    #             count -= 1
        
    #     return True

def main():
    sol = Solution()
    print(sol.kLengthApart(nums = [0,0,0,1,0,1], k = 2))
    print(sol.kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2))
    print(sol.kLengthApart(nums = [1,0,0,1,0,1], k = 2))

if __name__ == '__main__':
    main()