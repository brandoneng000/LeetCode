class Solution:
    def myAtoi(self, s: str) -> int:
        from string import digits
        s = s.lstrip()
        if not s: return 0

        negative = -1 if s[0] == '-' else 1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]

        if not s: return 0
        number = ""
        for digit in s:
            if digit in digits:
                number += digit
            else:
                break
        
        number = int(number) * negative if len(number) > 0 else 0
        number = -2 ** 31 if number < -2 ** 31 else number
        number = 2 ** 31 - 1 if number > 2 ** 31 - 1 else number

        return number
        
def main():
    sol = Solution()
    print(sol.myAtoi("4193 with words"))
    print(sol.myAtoi("          +42"))
    print(sol.myAtoi("          -918571986719867912986742"))
    print(sol.myAtoi("          -2147483646"))

if __name__ == '__main__':
    main()