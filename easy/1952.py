class Solution:
    def isThree(self, n: int) -> bool:
        count = 2

        for num in range(2, n - 1):
            if n % num == 0:
                count += 1
                if count > 3:
                    return False

        return count == 3

def main():
    sol = Solution()
    print(sol.isThree(2))
    print(sol.isThree(4))
    print(sol.isThree(8))
    print(sol.isThree(10 ** 4))

if __name__ == '__main__':
    main()