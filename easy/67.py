class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

        
def main():
    sol = Solution()
    print(sol.addBinary(a = "11", b = "1"))
    print(sol.addBinary(a = "1010", b = "1011"))

if __name__ == '__main__':
    main()