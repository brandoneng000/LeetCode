class Solution:
    def reverseDegree(self, s: str) -> int:
        z = ord('z')
        res = 0

        for i, c in enumerate(s, 1):
            res += i * (z - ord(c) + 1)

        return res


def main():
    sol = Solution()
    print(sol.reverseDegree("abc"))
    print(sol.reverseDegree("zaza"))

if __name__ == '__main__':
    main()