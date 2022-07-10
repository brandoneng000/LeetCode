class Solution:
    def fib(self, n: int) -> int:
        cur, prev = 0, 1

        for _ in range(n):
            temp = cur
            cur += prev
            prev = temp

        return cur

        
def main():
    sol = Solution()
    print(sol.fib(2))
    print(sol.fib(3))
    print(sol.fib(4))
    print(sol.fib(5))

if __name__ == '__main__':
    main()