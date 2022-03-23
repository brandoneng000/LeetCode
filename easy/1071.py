class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short = str1 if len(str1) < len(str2) else str2
        common = ""
        gcd = ""

        for letter in short:
            common += letter
            if len(str1) % len(common) == 0 and len(str2) % len(common) == 0:
                check_one = common * (len(str1) // len(common))
                check_two = common * (len(str2) // len(common))
                if check_one == str1 and check_two == str2:
                    gcd = common

        return gcd
        
def main():
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))
    print(sol.gcdOfStrings("ABABAB", "ABAB"))
    print(sol.gcdOfStrings("LEET", "CODE"))

if __name__ == '__main__':
    main()