class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        cur = 1

        for _ in range(n):
            temp = cur
            cur += prev
            prev = temp
        
        return cur
            


def main():
    sol = Solution()
    # print(sol.climbStairs(19))
    print(sol.climbStairs(1))
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(4))

if __name__ == '__main__':
    main()