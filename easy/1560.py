from typing import List
import itertools

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # marathon = dict.fromkeys([i for i in range(1, n + 1)], 0)

        # runner = rounds[0]
        # marathon[runner] += 1
        # for index in range(1, len(rounds)):
        #     lap = rounds[index] if runner < rounds[index] else rounds[index] + n

        #     for key in range(runner, lap):
        #         marathon[(key % n) + 1] += 1
            
        #     runner = rounds[index]
            
        # most_visited = max(marathon.values())
        # positions = [key for key in marathon.keys() if marathon[key] == most_visited]

        # return positions

        start = rounds[0]
        end = rounds[-1]

        if start <= end:
            return range(start, end + 1)
        else:
            return itertools.chain(range(1, end + 1), range(start, n + 1))
        


def main():
    sol = Solution()
    print(sol.mostVisited(n = 4, rounds = [1,3,1,2]))
    print(sol.mostVisited(n = 2, rounds = [2,1,2,1,2,1,2,1,2]))
    print(sol.mostVisited(n = 7, rounds = [1,3,5,7]))

if __name__ == '__main__':
    main()