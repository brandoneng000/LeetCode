from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)
        ops = {}
        res = nums[::]

        for x, y in reversed(operations):
            ops[x] = ops.get(y, y)

        for i in range(n):
            if res[i] in ops:
                res[i] = ops[res[i]]
            
        return res
        
def main():
    sol = Solution()
    print(sol.arrayChange(nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]))
    print(sol.arrayChange(nums = [1,2], operations = [[1,3],[2,1],[3,2]]))

if __name__ == '__main__':
    main()