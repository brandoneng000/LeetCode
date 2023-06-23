from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        seq = {}

        for i in range(len(nums)):
            for j in range(0, i):
                diff = nums[j] - nums[i]
                seq[(i, diff)] = seq.setdefault((j, diff), 1) + 1
        
        return max(seq.values())

def main():
    sol = Solution()
    print(sol.longestArithSeqLength([83,20,17,43,52,78,68,45]))
    print(sol.longestArithSeqLength([3,6,9,12]))
    print(sol.longestArithSeqLength([9,4,7,2,10]))
    print(sol.longestArithSeqLength([20,1,15,3,10,5,8]))

if __name__ == '__main__':
    main()