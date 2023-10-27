from typing import List
import collections

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 1000000007
        n = len(nums)
        count = [0] * (n + 1)
        res = 0

        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1

        for i in range(1, n + 1):
            count[i] += count[i - 1]
        
        for freq, num in zip(sorted(count[:-1]), sorted(nums)):
            res += freq * num
        
        return res % mod

    # def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
    #     mod = 1000000007
    #     nums.sort(reverse=True)
    #     request_count = collections.Counter()
    #     index = 0
    #     res = 0

    #     for start, end in requests:
    #         request_count += collections.Counter(range(start, end + 1))
        
    #     for r, count in request_count.most_common():
    #         res += count * nums[index]
    #         index += 1
        
    #     return res % mod


def main():
    sol = Solution()
    print(sol.maxSumRangeQuery(nums = [1,2,3,4,5], requests = [[1,3],[0,1]]))
    print(sol.maxSumRangeQuery(nums = [1,2,3,4,5,6], requests = [[0,1]]))
    print(sol.maxSumRangeQuery(nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]))

if __name__ == '__main__':
    main()