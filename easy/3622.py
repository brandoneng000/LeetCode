class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num_sum = 0
        num_prod = 1
        num = n

        while num:
            num, r = divmod(num, 10)
            num_sum += r
            num_prod *= r

        return n % (num_sum + num_prod) == 0


def main():
    sol = Solution()
    print(sol.checkDivisibility(99))
    print(sol.checkDivisibility(23))

if __name__ == '__main__':
    main()