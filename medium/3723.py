class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        res = [0] * num

        for i in range(num):
            res[i] += min(sum, 9)
            sum -= min(sum, 9)

        return "".join(str(d) for d in res)


def main():
    sol = Solution()
    print(sol.maxSumOfSquares(num = 2, sum = 3))
    print(sol.maxSumOfSquares(num = 2, sum = 17))
    print(sol.maxSumOfSquares(num = 1, sum = 10))

if __name__ == '__main__':
    main()