class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = ""
        while columnNumber:
            columnNumber -= 1
            char_value = (columnNumber % 26)
            columnNumber //= 26

            column = chr(char_value + ord('A')) + column

        return column

        
def main():
    sol = Solution()
    print(sol.convertToTitle(727))

if __name__ == '__main__':
    main()