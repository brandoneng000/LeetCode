from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums + nums
        result = [None] * (len(nums) * 2)
        
        for index in range(len(nums)):
            result[index] = nums[index]
            result[index + len(nums)] = nums[index]
            
        return result

def main():
    sol = Solution()
    print(sol.getConcatenation([1,2,1]))
    print(sol.getConcatenation([1,3,2,1]))

if __name__ == '__main__':
    main()