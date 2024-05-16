from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_day = {}
        cur_day = 1

        for task in tasks:
            if task in last_day and last_day[task] > cur_day:
                cur_day = last_day[task]
            last_day[task] = cur_day + space + 1
            cur_day += 1
        
        return cur_day - 1
        
def main():
    sol = Solution()
    print(sol.taskSchedulerII(tasks = [1,2,1,2,3,1], space = 3))
    print(sol.taskSchedulerII(tasks = [5,8,8,5], space = 2))

if __name__ == '__main__':
    main()