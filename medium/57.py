from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        
        result.append(newInterval)
        return result

def main():
    sol = Solution()
    print(sol.insert([[1,3],[6,9]], [2,5]))
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(sol.insert([], [5,7]))
    print(sol.insert([[1,5]], [6,8]))


if __name__ == '__main__':
    main()