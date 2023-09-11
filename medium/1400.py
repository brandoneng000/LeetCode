import collections

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(set(s)) == k:
            return True
        
        letter_count = collections.Counter(s)
        odds = 0

        for letter in letter_count:
            if letter_count[letter] % 2:
                odds += 1
        
        if odds <= k:
            return len(s) >= k
        else:
            return False


        
def main():
    sol = Solution()
    print(sol.canConstruct(s = "qlkzenwmmnpkopu", k = 15))
    print(sol.canConstruct(s = "annabelle", k = 2))
    print(sol.canConstruct(s = "leetcode", k = 3))
    print(sol.canConstruct(s = "true", k = 4))

if __name__ == '__main__':
    main()