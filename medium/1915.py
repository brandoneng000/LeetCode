from collections import Counter

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0
        count = Counter()
        count[0] += 1
        mask = 0

        for letter in word:
            shift = ord(letter) - 97
            mask ^= 1 << shift
            res += count[mask]

            for i in range(10):
                check = mask ^ (1 << i)
                res += count[check]
            
            count[mask] += 1
        
        return res

def main():
    sol = Solution()
    print(sol.wonderfulSubstrings("aba"))
    print(sol.wonderfulSubstrings("aabb"))
    print(sol.wonderfulSubstrings("he"))

if __name__ == '__main__':
    main()