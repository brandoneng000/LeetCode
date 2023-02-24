from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)

        for num in nums:
            if largest < 2 * num and largest != num:
                return -1
        
        return nums.index(largest)

def main():
    sol = Solution()
    print(sol.dominantIndex([3,6,1,0]))
    print(sol.dominantIndex([1,2,3,4]))

if __name__ == '__main__':
    main()