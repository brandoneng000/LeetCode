from typing import List

# class NumArray:
#     def __init__(self, nums: List[int]):
#         self.nums = {}
#         self.sums = { 0:0 }
#         self.diff = {}
#         for i, val in enumerate(nums):
#             self.nums[i] = val
#             self.sums[i + 1] = self.sums[i] + val

#     def update(self, index: int, val: int) -> None:
#         self.diff[index] = self.nums[index] - val

#     def sumRange(self, left: int, right: int) -> int:
#         difference = 0
#         for key in range(left, right + 1):
#             difference += self.diff.get(key, 0)

#         return self.sums[right + 1] - self.sums[left] - difference

class NumArray:
    def __init__(self, nums: List[int]):
        if len(nums) > 0:
            self.size = len(nums)
            self.tree = [0] * (self.size * 2)
            self.build_tree(nums)

    def build_tree(self, nums):
        j = 0
        for i in range(self.size, 2 * self.size):
            self.tree[i] = nums[j]
            j += 1
        
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        index += self.size
        self.tree[index] = val
        while index > 0:
            left, right = index, index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2
        

    def sumRange(self, left: int, right: int) -> int:
        left += self.size
        right += self.size
        total = 0
        while left <= right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1
            if right % 2 == 0:
                total += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        
        return total
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)