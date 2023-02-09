from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # forward, backward = 0, 0
        # loc = start
        # if destination < start:
        #     dest = destination + len(distance)
        # else:
        #     dest = destination

        # distance = distance + distance
        # while loc < dest:
        #     forward += distance[loc]
        #     loc += 1

        # if start < destination:
        #     loc = start + len(distance) // 2
        # else:
        #     loc = start
        # while loc > destination:
        #     backward += distance[loc - 1]
        #     loc -= 1

        # return min(forward, backward)

        smaller = min(start, destination)
        larger = max(start, destination)

        return min(sum(distance[smaller: larger]), sum(distance) - sum(distance[smaller: larger]))


def main():
    sol = Solution()
    print(sol.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
    print(sol.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))
    print(sol.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))
    # 7 + 16 + 11 + 3 + 6 = 33
    # 10 + 9 + 2 + 7 = 28 
    print(sol.distanceBetweenBusStops(distance = [3,6,7,2,9,10,7,16,11], start = 6, destination = 2))

if __name__ == '__main__':
    main()