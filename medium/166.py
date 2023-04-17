class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        res = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator // denominator)
        i = 0
        numerator = numerator % denominator
        demical = ''

        cache = { numerator: i }

        while numerator % denominator:
            numerator *= 10
            i += 1
            remainder = numerator % denominator
            demical += str(numerator // denominator)
            if remainder in cache:
                terminating = demical[:cache[remainder]]
                repeating = demical[cache[remainder]:]
                return f'{res}.{terminating}({repeating})'
            cache[remainder] = i
            numerator = remainder
        
        return f'{res}.{demical}'
        
def main():
    sol = Solution()
    print(sol.fractionToDecimal(1, 2))
    print(sol.fractionToDecimal(2, 1))
    print(sol.fractionToDecimal(4, 333))
    print(sol.fractionToDecimal(1, 17))

if __name__ == '__main__':
    main()