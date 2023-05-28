from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lengths = [0] * len(nums)
        count = [0] * len(nums)
        max_length = res = 0
        for i in range(len(nums)):
            lengths[i] = 1
            count[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[i] == lengths[j] + 1:
                        count[i] += count[j]
                    elif lengths[i] < lengths[j] + 1:
                        lengths[i] = lengths[j] + 1
                        count[i] = count[j]
            if max_length == lengths[i]:
                res += count[i]
            elif max_length < lengths[i]:
                max_length = lengths[i]
                res = count[i]
        
        return res
            
def main():
    sol = Solution()
    print(sol.findNumberOfLIS([1,3,5,4,7]))
    print(sol.findNumberOfLIS([2,2,2,2,2]))

if __name__ == '__main__':
    main()