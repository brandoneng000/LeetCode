from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        increments = 0
        double = 0

        for num in nums:
            cur_double = 0
            while num:
                if num % 2 == 1:
                    num -= 1
                    increments += 1
                else:
                    num //= 2
                    cur_double += 1
            double = max(double, cur_double)
        
        return increments + double
        
def main():
    sol = Solution()
    print(sol.minOperations([1,5]))
    print(sol.minOperations([2,2]))
    print(sol.minOperations([4,2,5]))

if __name__ == '__main__':
    main()