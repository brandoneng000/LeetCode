class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        return left << shift

def main():
    sol = Solution()
    print(sol.rangeBitwiseAnd(5, 7))
    print(sol.rangeBitwiseAnd(0, 0))
    print(sol.rangeBitwiseAnd(1, 2147483647))
    print(sol.rangeBitwiseAnd(600000000, 2147483645))

if __name__ == '__main__':
    main()