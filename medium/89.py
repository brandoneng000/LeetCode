from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]

        for i in range(n):
            for c in reversed(res):
                res += [(1 << i) ^ c]
            # res += [(1 << i) ^ c for c in reversed(res)]

        return res

def main():
    sol = Solution()
    print(sol.grayCode(2))
    print(sol.grayCode(1))
    print(sol.grayCode(3))

if __name__ == '__main__':
    main()