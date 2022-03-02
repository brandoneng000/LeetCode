class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        def get_int(num: str) -> int:
            number = 0
            
            for digit in num:
                number *= 10
                number += int(digit)
            
            return number

        return str(get_int(num1) + get_int(num2))

        
def main():
    sol = Solution()
    print(sol.addStrings("11", "123"))

if __name__ == '__main__':
    main()