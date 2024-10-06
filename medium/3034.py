from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        m, n = len(pattern), len(nums)
        conversion = []
        res = 0
        
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                conversion.append(1)
            elif nums[i + 1] == nums[i]:
                conversion.append(0)
            else:
                conversion.append(-1)
        
        for i in range(n - m):
            if conversion[i: i + m] == pattern:
                res += 1
        
        return res


def main():
    sol = Solution()
    print(sol.countMatchingSubarrays(nums = [1,2,3,4,5,6], pattern = [1,1]))
    print(sol.countMatchingSubarrays(nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]))

if __name__ == '__main__':
    main()