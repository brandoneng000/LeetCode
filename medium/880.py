class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        
        for c in reversed(s):
            k %= size
            if k == 0 and c.isalpha():
                return c
            
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1

    # def decodeAtIndex(self, s: str, k: int) -> str:
    #     decode = ""

    #     for c in s:
    #         if c.isalpha():
    #             decode += c
    #         else:
    #             if len(decode) * int(c) > k:
    #                 return decode[k % len(decode) - 1]
    #             else:
    #                 decode *= int(c)
            
    #         if len(decode) - 1 > k:
    #             break

    #     return decode[k - 1]
        

def main():
    sol = Solution()
    print(sol.decodeAtIndex(s = "leet2code3", k = 10))
    print(sol.decodeAtIndex(s = "ha22", k = 5))
    print(sol.decodeAtIndex(s = "a2345678999999999999999", k = 1))

if __name__ == '__main__':
    main()