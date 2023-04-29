class Solution:
    def bulbSwitch(self, n: int) -> int:
        # bulbs_on = 0
        # counter = 3

        # while n > 0:
        #     counter = 3 + (2 * bulbs_on)
        #     bulbs_on += 1
        #     n -= counter

        # return bulbs_on
        return int(n ** 0.5)


def main():
    sol = Solution()
    for i in range(100):
        print(sol.bulbSwitch(i), end=" ")
        if i % 9 == 0:
            print()

if __name__ == '__main__':
    main()