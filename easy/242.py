class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        return "".join(sorted(s)) == "".join(sorted(t))
        
def main():
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("rat", "car"))

if __name__ == "__main__":
    main()