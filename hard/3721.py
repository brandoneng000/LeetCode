from typing import List
from collections import Counter

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.size = 4 * n
        self.total = [0] * self.size
        self.min_vals = [0] * self.size
        self.max_vals = [0] * self.size

    def _pull(self, node: int):
        l, r = node * 2, node * 2 + 1

        self.total[node] = self.total[l] + self.total[r]
        self.min_vals[node] = min(self.min_vals[l], self.total[l] + self.min_vals[r])
        self.max_vals[node] = max(self.max_vals[l], self.total[l] + self.max_vals[r])
    
    def update(self, idx: int, val: int):
        def _update(node: int = 1, l: int = 0, r: int = self.n - 1):
            if l == r:
                self.total[node] = val
                self.min_vals[node] = val
                self.max_vals[node] = val
                return
            
            m = l + (r - l) // 2

            if idx <= m:
                _update(node * 2, l, m)
            else:
                _update(node * 2 + 1, m + 1, r)
            
            self._pull(node)
        
        return _update()
    
    def find_rightmost_prefix(self, target: int = 0) -> int:
        def _exist(node: int, sum_before: int):
            return self.min_vals[node] <= target - sum_before <= self.max_vals[node]
        
        def _find(node: int = 1, l: int = 0, r: int = self.n - 1, sum_before: int = 0):
            if not _exist(node, sum_before):
                return -1
            if l == r:
                return l
            
            m = l + (r - l) // 2
            l_child, r_child = node * 2, node * 2 + 1

            sum_before_right = self.total[l_child] + sum_before

            if _exist(r_child, sum_before_right):
                return _find(r_child, m + 1, r, sum_before_right)
            
            return _find(l_child, l, m, sum_before)
        
        return _find()

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        seg_tree = SegmentTree(n)
        first = {}

        for l in reversed(range(n)):
            num = nums[l]

            if num in first:
                seg_tree.update(first[num], 0)

            first[num] = l
            seg_tree.update(l, 1 if num % 2 == 0 else -1)

            r = seg_tree.find_rightmost_prefix(target=0)

            if r >= l:
                res = max(res, r - l + 1)
        
        return res
        
def main():
    sol = Solution()
    print(sol.longestBalanced([2,5,4,3]))
    print(sol.longestBalanced([3,2,2,5,4]))
    print(sol.longestBalanced([1,2,3,2]))

if __name__ == '__main__':
    main()