class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = base = 1
        while n > 9 * base * digit:
            n -= 9 * base * digit
            digit += 1
            base *= 10
        q, r = divmod(n - 1, digit)
        return int(str(base + q)[r])
        
        
        # if n < 10:
        #     return n
        # num = 10
        # s = "123456789"
        # while len(s) < n:
        #     s += str(num)
        #     num += 1
        
        # return int(s[n - 1])

def main():
    sol = Solution()
    print(sol.findNthDigit(3))
    print(sol.findNthDigit(11))
    print(sol.findNthDigit(1000))

if __name__ == '__main__':
    main()