from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        cur_max = 0

        for i in range(n):
            cur_max = max(cur_max, nums[i])
            res[i] = nums[i] + cur_max + res[i - 1]
        
        return res

        
def main():
    sol = Solution()
    print(sol.findPrefixScore([2,3,7,5,10]))
    print(sol.findPrefixScore([1,1,2,4,8,16]))

if __name__ == '__main__':
    main()