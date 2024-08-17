class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        j = 0

        for letter in str1:
            if letter == str2[j]:
                j += 1
            elif chr(((ord(letter) - ord('a') + 1) % 26 + ord('a'))) == str2[j]:
                j += 1
            
            if j == n:
                break
            
        return j == n
        
def main():
    sol = Solution()
    print(sol.canMakeSubsequence(str1 = "abc", str2 = "ad"))
    print(sol.canMakeSubsequence(str1 = "zc", str2 = "ad"))
    print(sol.canMakeSubsequence(str1 = "ab", str2 = "d"))

if __name__ == '__main__':
    main()