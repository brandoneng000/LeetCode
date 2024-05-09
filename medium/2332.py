from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        passenger = 0

        for bus in buses:
            cap = capacity

            while cap and passenger < len(passengers) and passengers[passenger] <= bus:
                passenger += 1
                cap -= 1
        
        if cap == 0:
            latest = passengers[passenger - 1]
        else:
            latest = buses[-1]
        
        booked = set(passengers)
        for seat in range(latest, -1, -1):
            if seat not in booked:
                return seat

        
def main():
    sol = Solution()
    print(sol.latestTimeCatchTheBus(buses = [3], passengers = [2,4], capacity = 2))
    print(sol.latestTimeCatchTheBus(buses = [10,20], passengers = [2,17,18,19], capacity = 2))
    print(sol.latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2))

if __name__ == '__main__':
    main()