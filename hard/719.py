from typing import List
from collections import Counter

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def helper(middle: int):
            left = 0
            count = 0
            
            for right in range(1, n):
                while nums[right] - nums[left] > middle:
                    left += 1
                
                count += right - left
            
            return count
        
        nums.sort()
        n = len(nums)
        left = 0
        right = max(nums)

        while left < right:
            middle = (left + right) // 2

            if helper(middle) >= k:
                right = middle
            else:
                left = middle + 1

        return right


    # def smallestDistancePair(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     distance_count = Counter()

    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             distance_count[abs(nums[i] - nums[j])] += 1
        
    #     for dist in sorted(distance_count):
    #         if distance_count[dist] < k:
    #             k -= distance_count[dist]
    #         else:
    #             return dist
        
def main():
    sol = Solution()
    print(sol.smallestDistancePair(nums = [1,3,1], k = 1))
    print(sol.smallestDistancePair(nums = [1,1,1], k = 2))
    print(sol.smallestDistancePair(nums = [1,6,1], k = 3))

if __name__ == '__main__':
    main()