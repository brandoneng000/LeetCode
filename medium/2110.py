from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        stack = []
        res = 0

        for p in prices:
            if stack and stack[-1] - 1 != p:
                res += sum(range(len(stack) + 1))
                stack = []
            stack.append(p)
        
        res += sum(range(len(stack) + 1))
        return res

        
def main():
    sol = Solution()
    print(sol.getDescentPeriods([3,2,1,4]))
    print(sol.getDescentPeriods([8,6,7,7]))
    print(sol.getDescentPeriods([1]))

if __name__ == '__main__':
    main()