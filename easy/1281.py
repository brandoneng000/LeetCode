import math


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = list(str(n))
        return math.prod([int(num) for num in s]) - sum([int(num) for num in s])

def main():
    sol = Solution()
    print(sol.subtractProductAndSum(234))
    print(sol.subtractProductAndSum(4421))

if __name__ == '__main__':
    main()