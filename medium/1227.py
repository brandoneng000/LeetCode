class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5

def main():
    sol = Solution()
    print(sol.nthPersonGetsNthSeat(1))
    print(sol.nthPersonGetsNthSeat(2))

if __name__ == '__main__':
    main()