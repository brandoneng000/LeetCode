from typing import List
from math import isqrt

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def check_prime(num: int):
            if num == 1:
                return False

            for i in range(2, isqrt(num) + 1):
                if num % i == 0:
                    return False
            
            return True
        
        n = len(nums)
        cache = set()
        left = right = -1

        for i in range(n):
            if nums[i] in cache:
                continue
            
            if check_prime(nums[i]):
                left = i
                break
            else:
                cache.add(nums[i])
        
        for i in range(n - 1, -1, -1):
            if nums[i] in cache:
                continue

            if check_prime(nums[i]):
                right = i
                break
            else:
                cache.add(nums[i])
        
        return right - left
        
def main():
    sol = Solution()
    print(sol.maximumPrimeDifference([4,2,9,5,3]))
    print(sol.maximumPrimeDifference([4,8,2,8]))

if __name__ == '__main__':
    main()