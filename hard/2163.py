from typing import List
from heapq import heappush, heappop, heapify

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3 = len(nums)
        n = n3 // 3

        part1 = [0] * (n + 1)
        total = sum(nums[:n])
        q1 = [-x for x in nums[:n]]
        heapify(q1)
        part1[0] = total

        for i in range(n, n * 2):
            total += nums[i]
            heappush(q1, -nums[i])
            total -= -heappop(q1)
            part1[i - (n - 1)] = total

        part2 = sum(nums[n * 2:])
        qr = nums[n * 2:]
        heapify(qr)
        res = part1[n] - part2

        for i in range(n * 2 - 1, n - 1, -1):
            part2 += nums[i]
            heappush(qr, nums[i])
            part2 -= heappop(qr)
            res = min(res, part1[i - n] - part2)
        
        return res
        
def main():
    sol = Solution()
    print(sol.minimumDifference([3,1,2]))
    print(sol.minimumDifference([7,9,5,8,1,3]))

if __name__ == '__main__':
    main()