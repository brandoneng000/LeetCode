from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            unique = set()
            for j in range(i, n):
                unique.add(nums[j])
                res += len(unique) ** 2
        
        return res
        
def main():
    sol = Solution()
    print(sol.sumCounts([1,2,1]))
    print(sol.sumCounts([1,1]))

if __name__ == '__main__':
    main()