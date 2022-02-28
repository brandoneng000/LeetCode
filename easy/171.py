class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        number_of_columns = len(columnTitle)
        
        for letter in columnTitle:
            number_of_columns -= 1

            if number_of_columns == 0:
                break
            
            column = (ord(letter) - ord("A") + 1) * (26 ** number_of_columns)
            column_number += column

        column_number += ord(columnTitle[-1]) - ord("A") + 1

        return column_number

def main():
    sol = Solution()
    print(sol.titleToNumber("A"))
    print(sol.titleToNumber("AB"))
    print(sol.titleToNumber("YZZ"))

if __name__ == "__main__":
    main()