from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start_val = 0
        min_val = 0

        for num in nums:
            start_val += num
            min_val = min(min_val, start_val)
            
        return abs(min_val) + 1

def main():
    sol = Solution()
    print(sol.minStartValue([-3,2,-3,4,2]))
    print(sol.minStartValue([1,2]))
    print(sol.minStartValue([1,-2,-3]))

if __name__ == '__main__':
    main()