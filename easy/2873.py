from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        def helper(cur: List[int], index: int):
            if len(cur) == 3:
                self.res = max(self.res, (cur[0] - cur[1]) * cur[2])
                return
            
            for i in range(index, n):
                cur.append(nums[i])
                helper(cur, i + 1)
                cur.pop()

        n = len(nums)
        self.res = 0
        helper([], 0)

        return self.res
        
def main():
    sol = Solution()
    print(sol.maximumTripletValue([12,6,1,2,7]))
    print(sol.maximumTripletValue([1,10,3,4,19]))
    print(sol.maximumTripletValue([1,2,3]))

if __name__ == '__main__':
    main()