from typing import List

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        nodes = 1
        level = 1

        while label >= nodes * 2:
            nodes *= 2
            level += 1

        while label != 0:
            res.append(label)
            level_max = 2 ** (level) - 1
            level_min = 2 ** (level - 1)
            label = (level_max + level_min - label) // 2
            level -= 1
        
        return res[::-1]


def main():
    sol = Solution()
    print(sol.pathInZigZagTree(14))
    print(sol.pathInZigZagTree(26))

if __name__ == '__main__':
    main()