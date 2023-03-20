from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        result = 0

        for num in nums:
            if smallest < num < largest:
                result += 1
        
        return result

def main():
    sol = Solution()
    print(sol.countElements([11,7,2,15]))
    print(sol.countElements([-3,3,3,90]))

if __name__ == '__main__':
    main()