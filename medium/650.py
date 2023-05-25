class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        d = 2
        while n > 1:
            while n % d == 0:
                res += d
                n /= d
            d += 1
        
        return res


def main():
    sol = Solution()
    print(sol.minSteps(30))
    print(sol.minSteps(3))
    print(sol.minSteps(1))

if __name__ == '__main__':
    main()