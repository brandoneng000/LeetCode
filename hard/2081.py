class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def create_palin(num: int, odd: bool):
            x = num

            if odd:
                x //= 10

            while x > 0:
                num = num * 10 + x % 10
                x //= 10
            
            return num

        def check_palin(num: int, base: int):
            digits = []

            while num:
                digits.append(num % base)
                num //= base
            
            return digits == digits[::-1]
        
        res = 0
        length = 1

        while n > 0:
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = create_palin(i, True)

                if check_palin(p, k):
                    res += p
                    n -= 1

            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = create_palin(i, False)

                if check_palin(p, k):
                    res += p
                    n -= 1
            
            length *= 10
        
        return res
        
def main():
    sol = Solution()
    print(sol.kMirror(k = 2, n = 5))
    print(sol.kMirror(k = 3, n = 7))
    print(sol.kMirror(k = 7, n = 17))

if __name__ == '__main__':
    main()