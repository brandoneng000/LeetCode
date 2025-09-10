class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k %= n
        
        return s[k:] + s[:k]
        
def main():
    sol = Solution()
    print(sol.getEncryptedString(s = "dart", k = 3))
    print(sol.getEncryptedString(s = "aaa", k = 1))

if __name__ == '__main__':
    main()