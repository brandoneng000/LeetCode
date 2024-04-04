from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def calc_trips(time: List[int], time_taken: int):
            res = 0

            for t in time:
                res += time_taken // t
            
            return res

        left, right = 0, totalTrips * min(time)

        while left < right:
            middle = (left + right) // 2
            trips = calc_trips(time, middle)

            if trips < totalTrips:
                left = middle + 1
            else:
                right = middle
        
        return left
        
def main():
    sol = Solution()
    print(sol.minimumTime(time = [1,2,3], totalTrips = 5))
    print(sol.minimumTime(time = [2], totalTrips = 1))

if __name__ == '__main__':
    main()