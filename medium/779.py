class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        middle = 2 ** (n - 2)
        if k <= middle:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - middle)

def main():
    sol = Solution()
    print(sol.kthGrammar(n = 1, k = 1))
    print(sol.kthGrammar(n = 2, k = 1))
    print(sol.kthGrammar(n = 2, k = 2))
    print(sol.kthGrammar(n = 30, k = 2))

if __name__ == '__main__':
    main()