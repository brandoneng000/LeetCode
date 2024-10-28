from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        cur = 0
        prev = -1

        for i in range(n):
            if nums[i] != prev:
                cur += 1
            else:
                res += (cur * (cur + 1)) // 2
                cur = 1
            
            prev = nums[i]
        
        return res + (cur * (cur + 1)) // 2
        
def main():
    sol = Solution()
    print(sol.countAlternatingSubarrays([0,1,1,1]))
    print(sol.countAlternatingSubarrays([1,0,1,0]))

if __name__ == '__main__':
    main()