from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        reach = [0] * (n + 1)

        for i in range(len(ranges)):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])
            reach[start] = max(reach[start], end)
        
        res = 0
        cur_end = 0
        next_end = 0

        for i in range(n + 1):
            if i > next_end:
                return -1

            if i > cur_end:
                res += 1
                cur_end = next_end
            
            next_end = max(next_end, reach[i])
        
        return res


def main():
    sol = Solution()
    print(sol.minTaps(n = 5, ranges = [3,4,1,1,0,0]))
    print(sol.minTaps(n = 3, ranges = [0,0,0,0]))

if __name__ == '__main__':
    main()