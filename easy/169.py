from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        n = len(nums) / 2
        
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            if num_dict[num] >= n:
                return num
        
def main():
    sol = Solution()
    print(sol.majorityElement([3,2,3]))
    print(sol.majorityElement([2,2,1,1,1,2,2]))

if __name__ == '__main__':
    main()