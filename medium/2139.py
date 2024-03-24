class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0

        while target != 1 and maxDoubles:
            if target % 2 == 1:
                res += 1
                target -= 1
            else:
                res += 1
                maxDoubles -= 1
                target //= 2

        return res + target - 1
        
def main():
    sol = Solution()
    print(sol.minMoves(5, 0))
    print(sol.minMoves(19, 2))
    print(sol.minMoves(10, 4))

if __name__ == '__main__':
    main()