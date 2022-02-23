from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
       self.num_array = nums 

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.num_array[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

def main():
    nums = NumArray([-2, 0, 3, -5, 2, -1])
    print(nums.sumRange(0, 2))

if __name__ == '__main__':
    main()