class Solution:
    def baseNeg2(self, n: int) -> str:
        if not n:
            return '0'
        
        res = []

        while n:
            remainder = n % -2
            n //= -2

            if remainder < 0:
                remainder += 2
                n += 1

            res.append(str(remainder))
        
        return "".join(res[::-1])

def main():
    sol = Solution()
    print(sol.baseNeg2(2))
    print(sol.baseNeg2(3))
    print(sol.baseNeg2(4))

if __name__ == '__main__':
    main()