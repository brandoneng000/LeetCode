from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cache = [-2] * (2 * len(nums) + 1)
        cache[len(nums)] = -1
        res = count = 0

        for i in range(len(nums)):
            count = count + (-1 if not nums[i] else 1)
            if cache[count + len(nums)] >= -1:
                res = max(res, i - cache[count + len(nums)])
            else:
                cache[count + len(nums)] = i
        
        return res

def main():
    sol = Solution()
    print(sol.findMaxLength([0,1]))
    print(sol.findMaxLength([0,1,0]))
    print(sol.findMaxLength([0,1,1,1,0,0]))

if __name__ == '__main__':
    main()