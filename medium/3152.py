from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n
        res = [False] * len(queries)

        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]
        
        for i in range(len(queries)):
            start = queries[i][0]
            end = queries[i][1]

            res[i] = prefix[end] - prefix[start] == 0

        return res
        
def main():
    sol = Solution()
    print(sol.isArraySpecial(nums = [1,4], queries = [[0,1]]))
    print(sol.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]))
    print(sol.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))

if __name__ == '__main__':
    main()