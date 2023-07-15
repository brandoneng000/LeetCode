from typing import List
import bisect

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        start_time = [event[0] for event in events]
        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(index: int, count: int):
            if count == 0 or index == n:
                return 0

            if dp[count][index] != -1:
                return dp[count][index]
            
            next_index = bisect.bisect_right(start_time, events[index][1])
            dp[count][index] = max(dfs(index + 1, count), events[index][2] + dfs(next_index, count - 1))
            return dp[count][index]

        return dfs(0, k)


    # def maxValue(self, events: List[List[int]], k: int) -> int:
    #     events.sort(key=lambda x: x[0])
    #     event_times = {}
    #     self.res = 0

    #     def pick_events(cur_events: List[List[int]], time: int):
    #         if len(cur_events) == k:
    #             self.res = max(self.res, sum(event[2] for event in cur_events))
    #             return
            
    #         if time not in event_times:
    #             event_times[time] = bisect.bisect(events, [time, ])
    #         index = event_times[time]

    #         while index < len(events):
    #             cur_events.append(events[index])
    #             pick_events(cur_events, events[index][1] + 1)
    #             cur_events.pop()
    #             index += 1
    #         self.res = max(self.res, sum(event[2] for event in cur_events))
        
    #     pick_events([], 0)
    #     return self.res


def main():
    sol = Solution()
    print(sol.maxValue(events = [[1,2,4],[3,4,3],[2,3,1]], k = 2))
    print(sol.maxValue(events = [[1,2,4],[3,4,3],[2,3,10]], k = 2))
    print(sol.maxValue(events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3))

if __name__ == '__main__':
    main()