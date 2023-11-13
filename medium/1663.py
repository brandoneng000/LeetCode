from string import ascii_lowercase

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n

        while k > 0:
            n -= 1
            res[n] = chr(ord('a') + min(25, k))
            k -= min(25, k)
        
        return "".join(res)

    # def getSmallestString(self, n: int, k: int) -> str:
    #     alphabet = { i: a for i, a in enumerate(ascii_lowercase, 1) }
    #     res = []

    #     while n:
    #         if k - 26 < n:
    #             res.append(alphabet[k - (n - 1)])
    #             res.extend('a' * (n - 1))
    #             break
    #         else:
    #             res.append(alphabet[26])
    #             k -= 26

    #         n -= 1
        
    #     return "".join(res[::-1])
        
def main():
    sol = Solution()
    print(sol.getSmallestString(n = 3, k = 27))
    print(sol.getSmallestString(n = 5, k = 73))

if __name__ == '__main__':
    main()