from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        n = len(nums)
        size = 2 << n.bit_length()

        self.tree = [[0] * (k + 1) for _ in range(size)]
        self.build(nums, 1, 0, n - 1)

    def make_leaf(self, o: int, value: int) -> None:
        info = [0] * (self.k + 1)
        r = value % self.k
        info[r] = 1
        info[self.k] = r
        self.tree[o] = info

    def merge_pre(self, left: List[int], right: List[int]) -> List[int]:
        pre = [0] * (self.k + 1)

        mul_l = left[self.k]
        mul_r = right[self.k]

        pre[self.k] = (mul_l * mul_r) % self.k

        for x in range(self.k):
            pre[x] = left[x]

        for x in range(self.k):
            pre[(mul_l * x) % self.k] += right[x]

        return pre

    def maintain(self, o: int) -> None:
        self.tree[o] = self.merge_pre(
            self.tree[o * 2],
            self.tree[o * 2 + 1],
        )

    def build(self, nums: List[int], o: int, l: int, r: int) -> None:
        if l == r:
            self.make_leaf(o, nums[l])
            return

        m = (l + r) // 2
        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)
        self.maintain(o)

    def update(self, o: int, l: int, r: int, index: int, value: int) -> None:
        if l == r:
            self.make_leaf(o, value)
            return

        m = (l + r) // 2

        if index <= m:
            self.update(o * 2, l, m, index, value)
        else:
            self.update(o * 2 + 1, m + 1, r, index, value)

        self.maintain(o)

    def query(self, o: int, l: int, r: int, L: int, R: int) -> List[int]:
        if L <= l and r <= R:
            return self.tree[o]

        m = (l + r) // 2

        if R <= m:
            return self.query(o * 2, l, m, L, R)
        if L > m:
            return self.query(o * 2 + 1, m + 1, r, L, R)

        left = self.query(o * 2, l, m, L, R)
        right = self.query(o * 2 + 1, m + 1, r, L, R)
        return self.merge_pre(left, right)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = SegmentTree(nums, k)
        res = []

        for index, value, start, x in queries:
            seg.update(1, 0, n - 1, index, value)
            pre = seg.query(1, 0, n - 1, start, n - 1)
            res.append(pre[x])

        return res

def main():
    sol = Solution()
    print(sol.resultArray(nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]))
    print(sol.resultArray(nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]))
    print(sol.resultArray(nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]))

if __name__ == '__main__':
    main()