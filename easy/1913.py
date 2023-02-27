from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = -float('inf')
        c = float('inf')

        for num in nums:
            if num > a:
                b = a
                a = num
            elif num > b:
                b = num
            
            if num < c:
                d = c
                c = num
            elif num < d:
                d = num
        
        return a * b - c * d

def main():
    sol = Solution()
    print(sol.maxProductDifference([5,6,2,7,4]))
    print(sol.maxProductDifference([4,2,5,9,7,4,8]))

if __name__ == '__main__':
    main()