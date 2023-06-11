from typing import List
import itertools

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1: -1]

        def helper(s: str):
            if not s or len(s) > 1 and s[0] == s[-1] == '0':
                return []
            if s[-1] == '0':
                return [s]
            if s[0] == '0':
                return [s[0] + '.' + s[1:]]
            return [s] + [s[: i] + '.' + s[i: ] for i in range(1, len(s))]

        return ['(%s, %s)' % (a, b) for i in range(len(s)) for a, b in itertools.product(helper(s[:i]), helper(s[i:]))]
        


def main():
    sol = Solution()
    print(sol.ambiguousCoordinates("(123)"))
    print(sol.ambiguousCoordinates("(0123)"))
    print(sol.ambiguousCoordinates("(00011)"))

if __name__ == '__main__':
    main()