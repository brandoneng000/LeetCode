from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # return event2[0] <= event1[1] <= event2[1] or event1[0] <= event2[1] <= event1[1]
        return event1[0] <= event2[1] and event2[0] <= event1[1]

def main():
    sol = Solution()
    print(sol.haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]))
    print(sol.haveConflict(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]))
    print(sol.haveConflict(event1 = ["01:20","03:00"], event2 = ["01:00","02:00"]))
    print(sol.haveConflict(event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]))

if __name__ == '__main__':
    main()