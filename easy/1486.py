class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start

        for _ in range(n - 1):
            start += 2
            result ^= start
        
        return result

def main():
    sol = Solution()
    print(sol.xorOperation(5, 0))
    print(sol.xorOperation(4, 3))

if __name__ == '__main__':
    main()