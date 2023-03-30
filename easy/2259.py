class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = ""
        
        for index, val in enumerate(number):
            if val == digit:
                res = max(res, number[:index] + number[index + 1:])
        
        return res

def main():
    sol = Solution()
    print(sol.removeDigit(number = "123", digit = "3"))
    print(sol.removeDigit(number = "1231", digit = "1"))
    print(sol.removeDigit(number = "551", digit = "5"))

if __name__ == '__main__':
    main()