from typing import List

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] != nums[i] + (j - i) % 2:
                    break
                res = max(res, j - i + 1)
        
        return res if res > 1 else -1

        
def main():
    sol = Solution()
    print(sol.alternatingSubarray([2,3,4,3,4]))
    print(sol.alternatingSubarray([4,5,6]))

if __name__ == '__main__':
    main()