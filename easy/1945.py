class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def helper(num: int, k: int):
            if k == 0:
                return num
            
            cur = 0

            while num:
                cur += num % 10
                num //= 10
            
            return helper(cur, k - 1)

        num = int(''.join(str(ord(letter) - ord('a') + 1) for letter in s))
        return helper(num, k)

        
    # def getLucky(self, s: str, k: int) -> int:
    #     s = list(s)

    #     for index in range(len(s)):
    #         s[index] = str(ord(s[index]) - ord('a') + 1)
        
    #     s = list(''.join(s))
        
    #     for _ in range(k):
    #         s = [int(digit) for digit in s]
    #         convert = sum(s)
    #         s = list(str(convert))
        
    #     return convert

    
def main():
    sol = Solution()
    print(sol.getLucky(s = "iiii", k = 1))
    print(sol.getLucky(s = "leetcode", k = 2))
    print(sol.getLucky(s = "zbax", k = 2))

if __name__ == '__main__':
    main()