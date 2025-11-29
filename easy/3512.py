from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        remainder = total % k

        return remainder
        
def main():
    sol = Solution()
    print(sol.minOperations(nums = [3,9,7], k = 5))
    print(sol.minOperations(nums = [4,1,3], k = 4))
    print(sol.minOperations(nums = [3,2], k = 6))

if __name__ == '__main__':
    main()