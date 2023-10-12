# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left = 1
        right = mountain_arr.length() - 2

        while left < right:
            middle = (left + right) // 2
            middle_mountain = mountain_arr.get(middle)
            right_middle = mountain_arr.get(middle + 1)

            if middle_mountain < right_middle:
                left = middle + 1
            else:
                right = middle

        peak = left

        if mountain_arr.get(peak) == target:
            return peak

        left = 0
        right = peak

        while left < right:
            middle = (left + right) // 2
            if mountain_arr.get(middle) < target:
                left = middle + 1
            else:
                right = middle
        
        if mountain_arr.get(left) == target:
            return left

        left = peak + 1
        right = mountain_arr.length() - 1

        while left < right:
            middle = (left + right) // 2
            
            if mountain_arr.get(middle) > target:
                left = middle + 1
            else:
                right = middle
        
        if mountain_arr.get(left) == target:
            return left

        return -1