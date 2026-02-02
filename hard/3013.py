from typing import List
from heapq import heappush, heappop, heapreplace

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        heap_used = []
        heap_unused = []
        used = set()
        s = 0
        res = 10 ** 26

        for right in range(1, n):
            left = right - dist - 1

            if left > 0 and left in used:
                used.remove(left)
                s -= nums[left]

                while heap_unused and heap_unused[0][1] < left:
                    heappop(heap_unused)
                
                if heap_unused:
                    num, i = heappop(heap_unused)
                    heappush(heap_used, (-num, i))
                    used.add(i)
                    s += num
            
            if len(used) < k - 1:
                heappush(heap_used, (-nums[right], right))
                used.add(right)
                s += nums[right]
            else:
                while heap_used[0][1] not in used:
                    heappop(heap_used)

                if nums[right] < -heap_used[0][0]:
                    num, i = heapreplace(heap_used, (-nums[right], right))
                    used.remove(i)
                    used.add(right)
                    s += num + nums[right]

                    heappush(heap_unused, (-num, i))
                else:
                    heappush(heap_unused, (nums[right], right))

            if left >= 0:
                res = min(s, res)
        
        return nums[0] + res

        
def main():
    sol = Solution()
    print(sol.minimumCost(nums = [1,3,2,6,4,2], k = 3, dist = 3))
    print(sol.minimumCost(nums = [10,1,2,2,2,1], k = 4, dist = 3))
    print(sol.minimumCost(nums = [10,8,18,9], k = 3, dist = 1))

if __name__ == '__main__':
    main()