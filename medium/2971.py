from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0
        res = -1

        for num in nums:
            if num < prev:
                res = num + prev
            prev += num
        
        return res
        

        
def main():
    sol = Solution()
    print(sol.largestPerimeter([1,1,2]))
    print(sol.largestPerimeter([5,5,5]))
    print(sol.largestPerimeter([1,12,1,2,5,50,3]))
    print(sol.largestPerimeter([5,5,50]))

if __name__ == '__main__':
    main()