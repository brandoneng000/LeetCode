class Solution:
    def generateTheString(self, n: int) -> str:
        res = ""

        if n % 2 == 1:
            return "a" * n
        else:
            return ("a" * (n - 1)) + "b"

def main():
    sol = Solution()
    print(sol.generateTheString(4))

if __name__ == '__main__':
    main()