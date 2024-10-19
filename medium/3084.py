class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        
        return count * (count + 1) // 2
                
        
def main():
    sol = Solution()
    print(sol.countSubstrings(s = "abada", c = "a"))
    print(sol.countSubstrings(s = "zzz", c = "z"))

if __name__ == '__main__':
    main()