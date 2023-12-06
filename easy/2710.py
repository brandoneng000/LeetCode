class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')

    # def removeTrailingZeros(self, num: str) -> str:
    #     n = len(num)
        
    #     while n > 1 and num[n - 1] == '0':
    #         n -= 1
        
    #     return num[:n]
        
def main():
    sol = Solution()
    print(sol.removeTrailingZeros("51230100"))
    print(sol.removeTrailingZeros("123"))

if __name__ == '__main__':
    main()