from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = nums[:]
        nums_dict = {}

        while temp:
            largest = max(temp)
            temp.remove(largest)
            nums_dict[largest] = len(temp) - temp.count(largest)
            
        for index in range(len(nums)):
            nums[index] = nums_dict[nums[index]]
        
        return nums
        

def main():
    sol = Solution()
    print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))
    print(sol.smallerNumbersThanCurrent([6,5,4,8]))
    print(sol.smallerNumbersThanCurrent([7,7,7,7]))

if __name__ == '__main__':
    main()