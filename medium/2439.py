from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        res = 0

        for i in range(n):
            total += nums[i]
            res = max(res, (total + i) // (i + 1))
        
        return res
        

def main():
    sol = Solution()
    print(sol.minimizeArrayValue([3,7,1,6]))
    print(sol.minimizeArrayValue([10,1]))

if __name__ == '__main__':
    main()