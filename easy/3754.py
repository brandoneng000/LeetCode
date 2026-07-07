class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digit_sum = 0
        digit_concat = []

        while n:
            n, r = divmod(n, 10)
            digit_sum += r

            if r != 0:
                digit_concat.append(str(r))
        
        if digit_concat:
            digit_concat = int(''.join(digit_concat[::-1]))
        else:
            return 0

        return digit_concat * digit_sum
        
def main():
    sol = Solution()
    print(sol.sumAndMultiply(0))
    print(sol.sumAndMultiply(10203004))
    print(sol.sumAndMultiply(1000))

if __name__ == '__main__':
    main()