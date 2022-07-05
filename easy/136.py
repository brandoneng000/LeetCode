from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = 0

        # Use XOR to find the only duplicate
        for num in nums:
            total ^= num

        return total
        

def main():
    sol = Solution()
    print(sol.singleNumber([2,2,1]))
    print(sol.singleNumber([4,1,2,1,2]))

if __name__ == '__main__':
    main()