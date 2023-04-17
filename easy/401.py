from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []

        for h in range(12):
            for m in range(60):
                if bin((h * 64) + m).count('1') == turnedOn:
                    res.append(f'{h}:{m:02d}')

        return res


def main():
    sol = Solution()
    print(sol.readBinaryWatch(1))
    print(sol.readBinaryWatch(2))
    # print(sol.readBinaryWatch(9))

if __name__ == '__main__':
    main()