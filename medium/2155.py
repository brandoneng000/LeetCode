from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        nums.append(0)
        n = len(nums)
        left = 0
        right = nums.count(1)
        cur_max = -1
        res = []

        for i in range(n):
            total = left + right

            if total == cur_max:
                res.append(i)
            elif total > cur_max:
                cur_max = total
                res = [i]
            
            left += nums[i] == 0
            right -= nums[i]
        
        return res


        
def main():
    sol = Solution()
    print(sol.maxScoreIndices([0,0,1,0]))
    print(sol.maxScoreIndices([0,0,0]))
    print(sol.maxScoreIndices([1,1]))

if __name__ == '__main__':
    main()