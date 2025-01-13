from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        
        return sum(1 if count[letter] % 2 else 2 for letter in count)

            
        
def main():
    sol = Solution()
    print(sol.minimumLength("abaacbcbb"))
    print(sol.minimumLength("aa"))

if __name__ == '__main__':
    main()