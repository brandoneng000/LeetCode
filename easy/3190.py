from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            num %= 3

            if num == 0:
                continue

            res += min(3 - num, num)
        
        return res
        
def main():
    sol = Solution()
    print(sol.minimumOperations([1,2,3,4]))
    print(sol.minimumOperations([3,6,9]))

if __name__ == '__main__':
    main()