class Solution:
    def isBalanced(self, num: str) -> bool:
        n = len(num)
        even = odd = 0

        for i in range(0, n, 2):
            even += int(num[i])
        
        for i in range(1, n, 2):
            odd += int(num[i])
        
        return even == odd
        
def main():
    sol = Solution()
    print(sol.isBalanced("1234"))
    print(sol.isBalanced("24123"))

if __name__ == '__main__':
    main()