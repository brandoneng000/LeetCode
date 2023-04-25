class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 0, sum(range(n + 1))
        for i in range(n + 1):
            left += i
            if left == right:
                return i
            right -= i

        return -1

def main():
    sol = Solution()
    print(sol.pivotInteger(8))
    print(sol.pivotInteger(1))
    print(sol.pivotInteger(4))

if __name__ == '__main__':
    main()