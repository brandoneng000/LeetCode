from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a = b = c = 0

        for i in range(n):
            a, b, c = b, c, min(a + 9, b + 4, c + 1) + costs[i]

        return c
        

def main():
    sol = Solution()
    print(sol.climbStairs(n = 4, costs = [1,2,3,4]))
    print(sol.climbStairs(n = 4, costs = [5,1,6,2]))
    print(sol.climbStairs(n = 3, costs = [9,8,3]))

if __name__ == '__main__':
    main()