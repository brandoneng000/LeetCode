from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []

        visited = set()
        min_heap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))

        while k > 0 and min_heap:
            val, (i, j) = heapq.heappop(min_heap)
            res.append((nums1[i], nums2[j]))

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))
            
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k -= 1

        return res

def main():
    sol = Solution()
    print(sol.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
    print(sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2))
    print(sol.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3))

if __name__ == '__main__':
    main()