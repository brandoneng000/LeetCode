from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = 0

        for n in nums:
            total += n
            while n:
                total -= n % 10
                n //= 10
        
        return abs(total)

def main():
    sol = Solution()
    print(sol.differenceOfSum([1,15,6,3]))
    print(sol.differenceOfSum([1,2,3,4]))

if __name__ == '__main__':
    main()