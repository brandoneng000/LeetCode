
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 1000000007
        count = [0] * 26

        for letter in s:
            count[ord(letter) - ord('a')] += 1

        for round in range(t):
            next = [0] * 26
            next[0] = count[25]
            next[1] = (count[25] + count[0]) % mod

            for i in range(2, 26):
                next[i] = count[i - 1]
            
            count = next

        return sum(count) % mod
    
def main():
    sol = Solution()
    print(sol.lengthAfterTransformations(s = "z", t = 25))
    print(sol.lengthAfterTransformations(s = "z", t = 26))
    print(sol.lengthAfterTransformations(s = "z", t = 27))
    print(sol.lengthAfterTransformations(s = "abcyy", t = 2))
    print(sol.lengthAfterTransformations(s = "azbk", t = 1))

if __name__ == '__main__':
    main()