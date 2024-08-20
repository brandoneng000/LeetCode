from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        evens1 = Counter(s1[i] for i in range(0, n, 2))
        evens2 = Counter(s2[i] for i in range(0, n, 2))
        odds1 = Counter(s1[i] for i in range(1, n, 2))
        odds2 = Counter(s2[i] for i in range(1, n, 2))

        return evens1 == evens2 and odds1 == odds2


        
def main():
    sol = Solution()
    print(sol.checkStrings(s1 = "abcdba", s2 = "cabdab"))
    print(sol.checkStrings(s1 = "abe", s2 = "bea"))

if __name__ == '__main__':
    main()