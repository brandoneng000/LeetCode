class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        first = min(s)
        last = max(s)

        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        if n == 2:
            return -1

        if s[0] == first or s[-1] == last:
            return 1

        for i in range(1, n - 1):
            if s[i] == first or s[i] == last:
                return 2
        
        return 3
            

def main():
    sol = Solution()
    print(sol.minOperations("dog"))
    print(sol.minOperations("card"))
    print(sol.minOperations("gf"))

if __name__ == '__main__':
    main()