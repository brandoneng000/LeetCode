class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) + int(coordinates[1])) % 2 == 1
        
def main():
    sol = Solution()
    print(sol.squareIsWhite("a1"))
    print(sol.squareIsWhite("h3"))
    print(sol.squareIsWhite("c7"))

if __name__ == '__main__':
    main()