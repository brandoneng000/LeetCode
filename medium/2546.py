class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target:
            return True
        
        if int(s, 2) == 0 or int(target, 2) == 0:
            return False
        
        return True
        
def main():
    sol = Solution()
    print(sol.makeStringsEqual(s = "1010", target = "0110"))
    print(sol.makeStringsEqual(s = "11", target = "00"))

if __name__ == '__main__':
    main()