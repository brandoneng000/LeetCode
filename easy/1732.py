from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0

        for trip in gain:
            altitude += trip
            max_altitude = max(max_altitude, altitude)

        return max_altitude
        

def main():
    sol = Solution()
    print(sol.largestAltitude([-5,1,5,0,-7]))
    print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))

if __name__ == '__main__':
    main()