class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
                "Jan": "01",
                "Feb": "02",
                "Mar": "03",
                "Apr": "04",
                "May": "05",
                "Jun": "06",
                "Jul": "07",
                "Aug": "08",
                "Sep": "09",
                "Oct": "10",
                "Nov": "11",
                "Dec": "12"
        }

        date = date.split()

        day = date[0][:-2] 
        
        if len(day) < 2:
            day = "0" + day
        
        return f"{date[2]}-{months[date[1]]}-{day}"

        
def main():
    sol = Solution()
    print(sol.reformatDate("20th Oct 2052"))
    print(sol.reformatDate("2nd Oct 2052"))
    print(sol.reformatDate("6th Jun 1933"))
    print(sol.reformatDate("26th May 1960"))

if __name__ == '__main__':
    main()