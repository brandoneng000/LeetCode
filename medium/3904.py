from typing import List

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_list = nums[::]
        max_list = nums[::]

        for i in range(n - 2, -1, -1):
            min_list[i] = min(min_list[i + 1], min_list[i])

        for i in range(1, n):
            max_list[i] = max(max_list[i - 1], max_list[i])

        for i in range(n):
            if max_list[i] - min_list[i] <= k:
                return i
        
        return -1

def main():
    sol = Solution()
    print(sol.firstStableIndex(nums = [5,0,1,4], k = 3))
    print(sol.firstStableIndex(nums = [3,2,1], k = 1))
    print(sol.firstStableIndex(nums = [0], k = 0))

if __name__ == '__main__':
    main()