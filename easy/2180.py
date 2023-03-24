class Solution:
    def countEven(self, num: int) -> int:
        res = 0

        for n in range(1, num + 1):
            if sum(int(digit) for digit in list(str(n))) % 2 == 0:
                res += 1

        return res


def main():
    sol = Solution()
    print(sol.countEven(4))
    print(sol.countEven(30))
    print(sol.countEven(13))

if __name__ == '__main__':
    main()