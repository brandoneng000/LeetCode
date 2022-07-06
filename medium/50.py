class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0
        res = 1
        n = abs(n)

        while n:
            if n % 2 == 1:
                res *= x
            
            x *= x
            n //= 2
        
        return res if not negative else (1 / res)

        


        
def main():
    sol = Solution()
    print(sol.myPow(2.0, 10))
    print(sol.myPow(2.1, 3))
    print(sol.myPow(2, -2))

if __name__ == '__main__':
    main()