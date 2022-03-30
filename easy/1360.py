class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        date1 = date1.split('-')
        date2 = date2.split('-')
        now = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
        later = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]))
        delta = later - now
        return abs(delta.days)

def main():
    sol = Solution()
    print(sol.daysBetweenDates("2019-06-29", "2019-06-30"))

if __name__ == '__main__':
    main()