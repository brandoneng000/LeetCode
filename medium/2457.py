class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def check_num(num: int):
            cur = 0

            while num:
                cur += num % 10
                num //= 10
            
            return cur <= target
        
        res = []
        cur = 0

        while not check_num(n):
            if n % 10 != 0:
                cur = 10 - (n % 10)
                res.append(str(cur))
                n += cur
            else:
                res.append('0')
            n //= 10
        
        return int(''.join(res[::-1])) if res else 0

        
def main():
    sol = Solution()
    print(sol.makeIntegerBeautiful(n = 16, target = 6))
    print(sol.makeIntegerBeautiful(n = 467, target = 6))
    print(sol.makeIntegerBeautiful(n = 1, target = 1))

if __name__ == '__main__':
    main()