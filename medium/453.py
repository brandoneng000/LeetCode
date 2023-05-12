from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
        # minimum = min(nums)
        # res = 0
        # for num in nums:
        #     res += num - minimum
            
        # return res

def main():
    sol = Solution()
    print(sol.minMoves([1,2,3]))
    print(sol.minMoves([1,2]))
    print(sol.minMoves([1,1,1]))

if __name__ == '__main__':
    main()