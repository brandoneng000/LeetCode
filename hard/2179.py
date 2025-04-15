from typing import List

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 2)

    def update(self, index: int, delta: int):
        index += 1

        while index <= self.n + 1:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index: int):
        res = 0
        index += 1

        while index > 0:
            res += self.tree[index]
            index -= index & -index
        
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = { nums2[i]: i for i in range(n) }

        mapped = [pos2[nums1[i]] for i in range(n)]
        res = 0

        bit_left = BIT(n)
        bit_right = BIT(n)
        right_count = [0] * n

        for i in range(n - 1, -1, -1):
            right_count[i] = bit_right.query(n - 1) - bit_right.query(mapped[i])
            bit_right.update(mapped[i], 1)
        
        for i in range(n):
            left = bit_left.query(mapped[i] - 1)
            right = right_count[i]
            res += left * right
            bit_left.update(mapped[i], 1)
        
        return res
        
def main():
    sol = Solution()
    print(sol.goodTriplets(nums1 = [2,0,1,3], nums2 = [0,1,2,3]))
    print(sol.goodTriplets(nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]))

if __name__ == '__main__':
    main()