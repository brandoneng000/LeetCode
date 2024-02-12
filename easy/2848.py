from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        n = len(nums)
        end = max(nums[i][1] for i in range(n))
        parking = [False for i in range(end + 1)]

        for start, end in nums:
            for i in range(start, end + 1):
                parking[i] = True
        
        return sum(parking)


def main():
    sol = Solution()
    print(sol.numberOfPoints([[3,6],[1,5],[4,7]]))
    print(sol.numberOfPoints([[1,3],[5,8]]))

if __name__ == '__main__':
    main()