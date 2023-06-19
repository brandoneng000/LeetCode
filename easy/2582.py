class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        q, r = divmod(time, n - 1)
        if q % 2 == 0:
            return r + 1
        return n - r

    # def passThePillow(self, n: int, time: int) -> int:
    #     nums = [i for i in range(1, n + 1)]
    #     nums += [i for i in range(n - 1, 1, -1)]
    #     return nums[time % len(nums)]

def main():
    sol = Solution()
    print(sol.passThePillow(n = 8, time = 17))
    print(sol.passThePillow(n = 8, time = 9))
    print(sol.passThePillow(n = 4, time = 5))
    print(sol.passThePillow(n = 3, time = 2))

if __name__ == '__main__':
    main()