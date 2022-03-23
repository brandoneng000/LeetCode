class Solution:
    def dayOfYear(self, date: str) -> int:
        date = [int(d) for d in date.split("-")]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        # days = date[2] + (1 if (date[0] % 4 == 0 and ((date[0] % 100 == 0 and date[0] % 400 == 0) or date[0] % 100 != 0)) and date[1] > 2 else 0) 
        days = date[2]
        days += sum(months[:date[1] - 1])
        days += int((date[0] % 4 == 0 and ((date[0] % 100 == 0 and date[0] % 400 == 0) or date[0] % 100 != 0)) and date[1] > 2)

        return days

def main():
    sol = Solution()
    print(sol.dayOfYear("2019-01-09"))
    print(sol.dayOfYear("1900-05-02"))

if __name__ == '__main__':
    main()