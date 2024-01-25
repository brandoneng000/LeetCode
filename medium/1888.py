class Solution:
    def minFlips(self, s: str) -> int:
        prev = 0
        start_one, start_zero = 0, 0
        start_one_odd, start_zero_odd = float('inf'), float('inf')
        odd = len(s) % 2

        for b in s:
            bit = int(b)
            if bit == prev:
                if odd:
                    start_zero_odd = min(start_zero_odd, start_one)
                    start_one_odd += 1
                start_one += 1
            else:
                if odd:
                    start_one_odd = min(start_one_odd, start_zero)
                    start_zero_odd += 1
                start_zero += 1
            prev = 1 - prev
        
        return min(start_one, start_zero, start_one_odd, start_zero_odd)


        
def main():
    sol = Solution()
    print(sol.minFlips("111000"))
    print(sol.minFlips("010"))
    print(sol.minFlips("1110"))

if __name__ == '__main__':
    main()