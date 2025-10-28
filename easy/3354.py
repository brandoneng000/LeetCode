from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = sum(nums)
        res = 0

        for i in range(n):
            if nums[i] == 0:
                if left == right:
                    res += 2
                else:
                    if left + 1 == right or left == right + 1:
                        res += 1
            left += nums[i]
            right -= nums[i]
        
        return res

        
def main():
    sol = Solution()
    print(sol.countValidSelections([1,0,2,0,3]))
    print(sol.countValidSelections([2,3,4,0,4,1,0]))

if __name__ == '__main__':
    main()