class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        res = []
        cur = 0
        letter_a = ord('a')

        for i in range(n):
            cur += ord(s[i]) - letter_a

            if i % k == k - 1:
                res.append(chr((cur % 26) + letter_a))
                cur = 0
        
        return ''.join(res)
            
        
def main():
    sol = Solution()
    print(sol.stringHash(s = "abcd", k = 2))
    print(sol.stringHash(s = "mxz", k = 3))

if __name__ == '__main__':
    main()