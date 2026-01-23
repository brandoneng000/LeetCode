from typing import List
from heapq import heappush, heappop, heapify
from itertools import pairwise

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)

        if all(x <= y for x, y in pairwise(nums)):
            return 0
        
        removed = [False] * n
        prev_num = [i - 1 for i in range(n)]
        next_num = [i + 1 if i + 1 < n else -1 for i in range(n)]

        heap = [(nums[i] + nums[i + 1], i) for i in range(n - 1)]
        heapify(heap)

        bad = sum(nums[i] > nums[i + 1] for i in range(n - 1))
        res = 0

        while bad > 0:
            total, i = heappop(heap)

            if removed[i] or next_num[i] == -1:
                continue

            j = next_num[i]
        
            if removed[j] or nums[i] + nums[j] != total:
                continue

            pi = prev_num[i]
            nj = next_num[j]

            if pi != -1 and nums[pi] > nums[i]:
                bad -= 1

            if nums[i] > nums[j]:
                bad -= 1

            if nj != -1 and nums[j] > nums[nj]:
                bad -= 1

            nums[i] = total
            removed[j] = True

            next_num[i] = nj

            if nj != -1:
                prev_num[nj] = i

            if pi != -1 and nums[pi] > nums[i]:
                bad += 1
            if nj != -1 and nums[i] > nums[nj]:
                bad += 1

            if pi != -1:
                heappush(heap, (nums[pi] + nums[i], pi))
            if nj != -1:
                heappush(heap, (nums[i] + nums[nj], i))
            res += 1
        
        return res

def main():
    sol = Solution()
    print(sol.minimumPairRemoval([5,2,3,1]))
    print(sol.minimumPairRemoval([1,2,2]))

if __name__ == '__main__':
    main()