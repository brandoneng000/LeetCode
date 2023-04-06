from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum_dict = {}

        for index in range(len(nums) - 1):
            total = nums[index] + nums[index + 1]
            sum_dict[total] = sum_dict.get(total, -1) + 1
            if sum_dict[total]:
                return True
        
        return False

def main():
    sol = Solution()
    print(sol.findSubarrays([4,2,4]))
    print(sol.findSubarrays([1,2,3,4,5]))
    print(sol.findSubarrays([0,0,0]))
    print(sol.findSubarrays([1,2,3,1,0,2]))

if __name__ == '__main__':
    main()