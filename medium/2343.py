from typing import List
from collections import defaultdict

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        num_size = len(nums[0])
        trims = defaultdict(list)
        res = [-1] * len(queries)

        for i, (k, trim) in enumerate(queries):
            trims[num_size - trim].append((k, i))
        
        for trim in sorted(trims):
            temp = [(num[trim:], i) for i, num in enumerate(nums)]
            temp.sort()
            for k, i in trims[trim]:
                res[i] = temp[k - 1][1]
        
        return res
            
        
def main():
    sol = Solution()
    print(sol.smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]))
    print(sol.smallestTrimmedNumbers(nums = ["24","37","96","04"], queries = [[2,1],[2,2]]))

if __name__ == '__main__':
    main()