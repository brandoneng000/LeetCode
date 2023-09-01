import collections

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        count = collections.Counter()
        left = 0

        for right in range(n):
            count[s[right]] += 1

            if len(count) == 3:
                while len(count) == 3:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        count.pop(s[left])
                    left += 1
                
                    res += n - right
        
        return res
        
def main():
    sol = Solution()
    print(sol.numberOfSubstrings("acbbcac"))
    print(sol.numberOfSubstrings("abcabc"))
    print(sol.numberOfSubstrings("aaacb"))
    print(sol.numberOfSubstrings("abc"))

if __name__ == '__main__':
    main()