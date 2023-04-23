class Solution:
    def countTime(self, time: str) -> int:
        hours, minutes = time.split(':')
        hour_choice = 1
        minute_choice = 1
        if '?' in hours:
            if '??' == hours:
                hour_choice = 24
            else:
                if hours[1] == '?':
                    hour_choice = 10 if int(hours[0]) != 2 else 4
                else:
                    if hours[1] == '4':
                        hour_choice = 3 if minute_choice == '00' else 2
                    else:
                        hour_choice = 3 if int(hours[1]) < 5 else 2
        if '?' in minutes:
            if '?' == minutes[0]:
                minute_choice *= 6
            if '?' == minutes[1]:
                minute_choice *= 10
        
        return hour_choice * minute_choice


def main():
    sol = Solution()
    print(sol.countTime("?5:00"))
    print(sol.countTime("0?:0?"))
    print(sol.countTime("??:??"))
    print(sol.countTime("2?:??"))

if __name__ == '__main__':
    main()