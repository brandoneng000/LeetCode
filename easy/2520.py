class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % int(digit) == 0 for digit in str(num))
        # res = 0
        # n = num
        # while n:
        #     res += num % (n % 10) == 0
        #     n //= 10
        
        # return res

def main():
    sol = Solution()
    print(sol.countDigits(7))
    print(sol.countDigits(121))
    print(sol.countDigits(1248))

if __name__ == '__main__':
    main()