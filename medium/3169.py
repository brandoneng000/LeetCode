from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)
        meetings.sort()
        res = meetings[0][0] - 1

        for i in range(1, n):
            if meetings[i][0] <= meetings[i - 1][1]:
                if meetings[i][1] < meetings[i - 1][1]:
                    meetings[i][1] = meetings[i - 1][1]
            else:
                res += meetings[i][0] - meetings[i - 1][1] - 1
        
        return res + days - meetings[-1][1]


    # def countDays(self, days: int, meetings: List[List[int]]) -> int:
    #     # days initialize to 0 - (days + 2)
    #     meeting_days = [0] * (days + 2)

    #     for start, end in meetings:
    #         meeting_days[start] += 1
    #         meeting_days[end + 1] -= 1
        
    #     for i in range(1, days + 2):
    #         meeting_days[i] += meeting_days[i - 1]
        
    #     # counts days starting from 1 to (# of days)
    #     return sum(meeting_days[i] == 0 for i in range(1, days + 1))
        
def main():
    sol = Solution()
    print(sol.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
    print(sol.countDays(days = 5, meetings = [[2,4],[1,3]]))
    print(sol.countDays(days = 6, meetings = [[1,6]]))

if __name__ == '__main__':
    main()