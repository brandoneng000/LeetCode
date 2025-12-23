class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
        year = bin(int(year))[2:]
        month = bin(int(month))[2:]
        day = bin(int(day))[2:]

        return '-'.join([year, month, day])
        
def main():
    sol = Solution()
    print(sol.convertDateToBinary("2080-02-29"))
    print(sol.convertDateToBinary("1900-01-01"))

if __name__ == '__main__':
    main()