class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = list(range(n)) + list(range(n - 2, 0, -1))
        return children[k % len(children)]
        
def main():
    sol = Solution()
    print(sol.numberOfChild(n = 3, k = 5))
    print(sol.numberOfChild(n = 5, k = 6))
    print(sol.numberOfChild(n = 4, k = 2))

if __name__ == '__main__':
    main()