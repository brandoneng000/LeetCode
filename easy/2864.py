class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = 0

        for bit in s:
            ones += int(bit)
        
        return "".join(['1'] * (ones - 1) + ['0'] * (n - ones) + ['1'])
        
def main():
    sol = Solution()
    print(sol.maximumOddBinaryNumber("010"))
    print(sol.maximumOddBinaryNumber("0101"))

if __name__ == '__main__':
    main()