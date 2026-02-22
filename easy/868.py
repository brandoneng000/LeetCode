class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        n = len(binary)
        left = 0
        res = 0

        while left < n and binary[left] == '0':
            left += 1

        for right in range(left + 1, n):
            if binary[right] == '1':
                res = max(res, right - left)
                left = right
        
        return res

    # def binaryGap(self, n: int) -> int:
    #     result = -1
    #     count = -1
        
    #     while n:
    #         if n & 1:
    #             result = max(result, count, 0)
    #             count = 1
    #         elif count != -1:
    #             count += 1
    #         n >>= 1

    #     return result


def main():
    sol = Solution()
    print(sol.binaryGap(22))
    print(sol.binaryGap(8))
    print(sol.binaryGap(5))

if __name__ == '__main__':
    main()