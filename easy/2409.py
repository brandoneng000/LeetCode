class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        if leaveAlice < arriveBob or leaveBob < arriveAlice:
            return 0
        
        arrive = max(arriveAlice, arriveBob).split('-')
        leave = min(leaveAlice, leaveBob).split('-')
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        arrive = sum(months[:int(arrive[0]) - 1]) + int(arrive[1])
        leave = sum(months[:int(leave[0]) - 1]) + int(leave[1])
        return leave - arrive + 1

def main():
    sol = Solution()
    print(sol.countDaysTogether(arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"))
    print(sol.countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))
    print(sol.countDaysTogether(arriveAlice = "10-20", leaveAlice = "12-22", arriveBob = "06-21", leaveBob = "07-05"))
    print(sol.countDaysTogether(arriveAlice = "09-01", leaveAlice = "10-19", arriveBob ="06-19", leaveBob = "10-20"))
    print(sol.countDaysTogether(arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-16"))


if __name__ == '__main__':
    main()