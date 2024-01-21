class Solution:
    def minSwaps(self, s: str) -> int:
        def gen_bits(start: str, alts: int):
            alternate = [start] * n
            alt_bit = '0' if start == '1' else '1'

            for i in range(1, n, 2):
                alternate[i] = alt_bit
            
            return ''.join(alternate)

        def bit_swaps(original: str, alt: str):
            diff = 0

            for i in range(n):
                if original[i] != alt[i]:
                    diff += 1
            
            return diff // 2
        
        n = len(s)
        ones = s.count('1')
        zeroes = n - ones

        if abs(ones - zeroes) > 1:
            return -1

        if ones > zeroes:
            alternate = gen_bits('1', zeroes)
        elif zeroes > ones:
            alternate = gen_bits('0', ones)
        else:
            return min(bit_swaps(s, gen_bits('0', ones)), bit_swaps(s, gen_bits('1', zeroes)))
        
        return bit_swaps(s, alternate)
        
def main():
    sol = Solution()
    print(sol.minSwaps("1110000"))
    print(sol.minSwaps("111000"))
    print(sol.minSwaps("010"))
    print(sol.minSwaps("1110"))

if __name__ == '__main__':
    main()