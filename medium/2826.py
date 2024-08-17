from typing import List
from bisect import bisect_right

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        longest = []

        for num in nums:
            if not longest or longest[-1] <= num:
                longest.append(num)
            else:
                index = bisect_right(longest, num)
                longest[index] = num
        
        return n - len(longest)
        
def main():
    sol = Solution()
    print(sol.minimumOperations([2,1,3,2,1]))
    print(sol.minimumOperations([1,3,2,1,3,3]))
    print(sol.minimumOperations([2,2,2,2,3,3]))

if __name__ == '__main__':
    main()