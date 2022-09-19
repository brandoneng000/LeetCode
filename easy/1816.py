class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])

def main():
    sol = Solution()
    print(sol.truncateSentence("Hello how are you Contestant", 4))
    print(sol.truncateSentence("What is the solution to this problem", 4))

if __name__ == '__main__':
    main()