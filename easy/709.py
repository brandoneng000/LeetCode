class Solution:
    def toLowerCase(self, s: str) -> str:
        lower = ""
        
        for letter in s:
            val = ord(letter)
            if 64 < val < 91:
                val += 32
                lower += chr(val)
            else:
                lower += letter

        return lower

def main():
    sol = Solution()
    print(sol.toLowerCase("Hello"))

if __name__ == '__main__':
    main()