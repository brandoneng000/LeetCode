class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        license = ""

        s = s.upper().replace("-", "")
        index = 0
        offset = 0
        while (len(s) - len(license)) % k != 0:
            license += s[index]
            index += 1
            offset = k
        
        while index < len(s):
            if (offset / k) == 1:
                license += "-"
                offset = 0
            license += s[index]
            index += 1
            offset += 1

        return license

        
def main():
    sol = Solution()
    print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))
    print(sol.licenseKeyFormatting("2-5g-3-J", 2))
    print(sol.licenseKeyFormatting("2", 2))

if __name__ == '__main__':
    main()