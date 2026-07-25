class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = max2 = 0

        while n:
            n, r = divmod(n, 10)

            if r > max1:
                max2 = max1
                max1 = r
            elif r > max2:
                max2 = r

        return max1 * max2
                

def main():
    sol = Solution()
    print(sol.maxProduct(31))
    print(sol.maxProduct(22))
    print(sol.maxProduct(124))

if __name__ == '__main__':
    main()