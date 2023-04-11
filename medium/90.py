from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def recursive(size: int, cur: List[int], index: int, arr: List[List[int]]):
            if len(cur) == size and cur not in arr:
                arr.append(cur.copy())
                return
            
            for i in range(index, len(nums)):
                cur.append(nums[i])
                recursive(size, cur, i + 1, arr)
                cur.pop()

        for i in range(len(nums) + 1):
            recursive(i, [], 0, res)
        
        return res

def main():
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2]))
    print(sol.subsetsWithDup([0]))
    print(sol.subsetsWithDup([4,4,4,1,4]))

if __name__ == '__main__':
    main()