from typing import List
import collections

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums_count = collections.Counter(nums)
        result = 0

        for key in nums_count:
            result += nums_count.get(key, 0) * nums_count.get(key + k, 0)

        return result



def main():
    sol = Solution()
    print(sol.countKDifference(nums = [1,2,2,1], k = 1))
    print(sol.countKDifference(nums = [1,2,2,1,3,3,3], k = 1))
    print(sol.countKDifference(nums = [1,3], k = 3))
    print(sol.countKDifference(nums = [3,2,1,5,4], k = 2))

if __name__ == '__main__':
    main()