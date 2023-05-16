from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = set()

        def helper(cur: List[int], index: int):
            for i in range(index, len(nums)):
                if nums[i] >= cur[-1]:
                    cur.append(nums[i])
                    self.res.add(tuple(cur.copy()))
                    helper(cur, i + 1)
                    cur.pop()

        cur = []
        for i in range(len(nums)):
            cur.append(nums[i])
            helper(cur, i + 1)
            cur.pop()
        
        return list(self.res)

def main():
    sol = Solution()
    print(sol.findSubsequences([4,6,7,7]))
    print(sol.findSubsequences([4,4,3,2,1]))

if __name__ == '__main__':
    main()