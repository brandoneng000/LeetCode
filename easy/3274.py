class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        letter1 = (ord(coordinate1[0]) - ord('a')) % 2
        num1 = int(coordinate1[1]) % 2

        letter2 = (ord(coordinate2[0]) - ord('a')) % 2
        num2 = int(coordinate2[1]) % 2

        if num1 == num2 and letter1 == letter2:
            return True
        
        if num1 != num2 and letter1 != letter2:
            return True
        
        return False

        
def main():
    sol = Solution()
    print(sol.checkTwoChessboards(coordinate1 = "a1", coordinate2 = "c3"))
    print(sol.checkTwoChessboards(coordinate1 = "a1", coordinate2 = "h3"))

if __name__ == '__main__':
    main()