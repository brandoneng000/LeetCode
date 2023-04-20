class Solution:
    def toHex(self, num: int) -> str:
        def two_complement(num: int):
            mask = 0b11111111111111111111111111111111
            num = num ^ mask
            return num + 1

        if not num: return '0'
        hex_dict = { 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f' }
        if num < 0:
            num = abs(num)
            num = two_complement(num)
        else:
            num = abs(num)
        res = []

        while num:
            remainder = str(num % 16) if num % 16 < 10 else hex_dict[num % 16]
            res = [remainder] + res
            num //= 16

        return "".join(res)


def main():
    sol = Solution()
    print(sol.toHex(26))
    print(sol.toHex(3205))
    print(sol.toHex(-1))

if __name__ == '__main__':
    main()