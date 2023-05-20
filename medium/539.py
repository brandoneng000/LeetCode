from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []

        for t in timePoints:
            temp = t.split(':')
            times.append(int(temp[0]) * 60 + int(temp[1]))
        
        times.sort()
        res = float('inf')
        for i in range(len(times) - 1):
            res = min(res, abs(times[i] - times[i + 1]))
        res = min(res, (times[0] + 1440) - times[-1])

        return res


def main():
    sol = Solution()
    print(sol.findMinDifference(["23:59","00:00"]))
    print(sol.findMinDifference(["00:00","23:59","00:00"]))

if __name__ == '__main__':
    main()