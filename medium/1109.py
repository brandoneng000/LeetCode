from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * (n + 1)

        for start, end, seats in bookings:
            flights[start - 1] += seats
            flights[end] -= seats
        
        for i in range(1, n):
            flights[i] += flights[i - 1]
        
        return flights[:-1]
        
        # flights = [0] * n

        # for start, end, seats in bookings:
        #     for flight in range(start - 1, end):
        #         flights[flight] += seats

        # return flights

def main():
    sol = Solution()
    print(sol.corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))
    print(sol.corpFlightBookings(bookings = [[1,2,10],[2,2,15]], n = 2))

if __name__ == '__main__':
    main()