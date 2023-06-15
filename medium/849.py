from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        go_left = [0] * len(seats)
        go_right = [0] * len(seats)
        go_right[0] = 1 if seats[0] == 0 else 0
        go_left[-1] = 1 if seats[-1] == 0 else 0

        for i in range(1, len(seats)):
            if seats[i] == 0:
                go_right[i] = go_right[i - 1] + 1
        # print(go_right)
        for i in range(len(seats) - 2, -1, -1):
            if seats[i] == 0:
                go_left[i] = go_left[i + 1] + 1
        # print(go_left)
        distance = []
        for index, (i, j) in enumerate(zip(go_left, go_right)):
            if index == 0 or index == len(go_left) - 1:
                distance.append(max(i, j))
            else:
                distance.append(min(i, j))

        return max(distance)

def main():
    sol = Solution()
    print(sol.maxDistToClosest([1,0,0,0,1,0,1]))
    print(sol.maxDistToClosest([1,0,0,0]))
    print(sol.maxDistToClosest([0,1]))

if __name__ == '__main__':
    main()