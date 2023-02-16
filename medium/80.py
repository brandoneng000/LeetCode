from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        end = len(nums)
        cur = nums[0]
        num_count = 1

        while index < end:
            if cur == nums[index]:
                num_count += 1
                if num_count > 2:
                    nums.pop(index)
                    num_count -= 1
                    end -= 1
                    index -= 1
            else:
                cur = nums[index]
                num_count = 1
            
            index += 1
        
        return len(nums)

def main():
    sol = Solution()
    print(sol.removeDuplicates([1,1,1,2,2,3]))
    print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))

if __name__ == '__main__':
    main()