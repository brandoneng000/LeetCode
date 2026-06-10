from typing import List
from heapq import heapreplace

class SparseTable:
    def __init__(self, nums: List[int]):
        n = len(nums)
        bit_width = n.bit_length()
        self.minn = [[0] * n for _ in range(bit_width)]
        self.maxx = [[0] * n for _ in range(bit_width)]

        for i in range(n):
            self.minn[0][i] = self.maxx[0][i] = nums[i]
        
        for i in range(1, bit_width):
            for j in range(n - (1 << i) + 1):
                self.minn[i][j] = min(self.minn[i - 1][j], self.minn[i - 1][j + (1 << (i - 1))])
                self.maxx[i][j] = max(self.maxx[i - 1][j], self.maxx[i - 1][j + (1 << (i - 1))])
    
    def query(self, left: int, right: int):
        k = (right - left).bit_length() - 1

        return (
            max(self.maxx[k][left], self.maxx[k][right - (1 << k)])
            - min(self.minn[k][left], self.minn[k][right - (1 << k)])
        )

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LUT = SparseTable(nums)
        res = 0

        pq = [(-LUT.query(i, n), i, n) for i in range(n)]

        for _ in range(k):
            val, l, r = pq[0]

            if val == 0:
                break

            res -= val
            heapreplace(pq, (-LUT.query(l, r - 1), l, r - 1))

        return res

        
def main():
    sol = Solution()
    print(sol.maxTotalValue(nums = [1,3,2], k = 2))
    print(sol.maxTotalValue(nums = [4,2,5,1], k = 3))

if __name__ == '__main__':
    main()