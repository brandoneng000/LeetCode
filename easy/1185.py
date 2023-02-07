class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leaps = max(0, (year - 1972) // 4 + 1)

        total_days = ((year - 1971) * 365) + leaps
        if year == 2100 and month > 2:
            total_days -= 1

        total_days += sum(days_per_month[:month - 1])
        if year % 4 == 0 and month <= 2:
            total_days -= 1

        total_days += day
        
        return week[total_days % 7]



def main():
    sol = Solution()
    print(sol.dayOfTheWeek(day = 31, month = 8, year = 2019))
    print(sol.dayOfTheWeek(day = 18, month = 7, year = 1999))
    print(sol.dayOfTheWeek(day = 15, month = 8, year = 1993))
    print(sol.dayOfTheWeek(day = 1, month = 1, year = 1971))
    print(sol.dayOfTheWeek(day = 2, month = 1, year = 1971))
    print(sol.dayOfTheWeek(day = 2, month = 6, year = 2023))
    print(sol.dayOfTheWeek(day = 29, month = 2, year = 2016))
    print(sol.dayOfTheWeek(day = 28, month = 2, year = 2016))


if __name__ == '__main__':
    main()