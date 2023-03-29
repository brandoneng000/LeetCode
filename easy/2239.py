from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = float('inf')

        for num in nums:
            if abs(res) > abs(num):
                res = num
            elif abs(res) == abs(num):
                res = max(res, num)

        return res

def main():
    sol = Solution()
    print(sol.findClosestNumber([-4,-2,1,4,8]))
    print(sol.findClosestNumber([2,-1,1]))

if __name__ == '__main__':
    main()