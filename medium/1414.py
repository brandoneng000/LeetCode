class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def calc_fib(goal: int) -> int:
            fib = [1, 1]

            while fib[-1] + fib[-2] <= goal:
                fib[0], fib[1] = fib[1], fib[0] + fib[1]
            
            return fib[1]
        
        res = 0
        
        while k:
            res += 1
            k -= calc_fib(k)
        
        return res



def main():
    sol = Solution()
    print(sol.findMinFibonacciNumbers(7))
    print(sol.findMinFibonacciNumbers(10))
    print(sol.findMinFibonacciNumbers(19))

if __name__ == '__main__':
    main()