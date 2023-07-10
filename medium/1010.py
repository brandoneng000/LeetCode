from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        minutes = [0] * 60
        res = 0

        for t in time:
            res += minutes[-t % 60]
            minutes[t % 60] += 1
        
        return res

    # def numPairsDivisibleBy60(self, time: List[int]) -> int:
    #     pairs = {}
    #     res = 0

    #     for t in time:
    #         res += pairs.get(-t % 60, 0)
    #         pairs[t % 60] = pairs.get(t % 60, 0) + 1
        
    #     return res

    # def numPairsDivisibleBy60(self, time: List[int]) -> int:
    #     res = 0

    #     for i in range(len(time)):
    #         for j in range(i + 1, len(time)):
    #             if (time[i] + time[j]) % 60 == 0:
    #                 res += 1
        
    #     return res

def main():
    sol = Solution()
    print(sol.numPairsDivisibleBy60([30,20,150,100,40]))
    print(sol.numPairsDivisibleBy60([60,60,60]))

if __name__ == '__main__':
    main()