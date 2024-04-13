from collections import deque

class Solution:
    def numberOfWays(self, s: str) -> int:
        left_ones, right_ones = 0, 0
        left_zeroes, right_zeroes = 0, 0
        res = 0

        for b in s:
            right_ones += b == '1'
            right_zeroes += b == '0'
        
        for b in s:
            if b == '0':
                res += left_ones * right_ones
                left_zeroes += 1
                right_zeroes -= 1
            else:
                res += left_zeroes * right_zeroes
                left_ones += 1
                right_ones -= 1

        return res

        
def main():
    sol = Solution()
    print(sol.numberOfWays("001101"))
    print(sol.numberOfWays("11100"))

if __name__ == '__main__':
    main()