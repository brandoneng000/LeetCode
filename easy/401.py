from typing import List
from itertools import combinations

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        leds = [
            (8, 'h'), (4, 'h'), (2, 'h'), (1, 'h'),
            (32, 'm'), (16, 'm'), (8, 'm'), (4, 'm'), (2, 'm'), (1, 'm')
        ]
        res = []

        for time in combinations(leds, turnedOn):
            hours = 0
            minutes = 0

            for val, unit in time:
                if unit == 'h':
                    hours += val
                else:
                    minutes += val

            if hours < 12 and minutes < 60:
                res.append(f'{hours}:{minutes:02d}')
        
        return res

    # def readBinaryWatch(self, turnedOn: int) -> List[str]:
    #     res = []

    #     for h in range(12):
    #         for m in range(60):
    #             if bin((h * 64) + m).count('1') == turnedOn:
    #                 res.append(f'{h}:{m:02d}')

    #     return res


def main():
    sol = Solution()
    print(sol.readBinaryWatch(1))
    print(sol.readBinaryWatch(2))
    # print(sol.readBinaryWatch(9))

if __name__ == '__main__':
    main()