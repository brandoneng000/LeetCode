class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary = set()

        for i in range(len(s) - k + 1):
            binary.add(s[i:i + k])
        
        return len(binary) == 2 ** k
        

def main():
    sol = Solution()
    print(sol.hasAllCodes(s = "00110", k = 2))
    print(sol.hasAllCodes(s = "00110110", k = 2))
    print(sol.hasAllCodes(s = "0110", k = 1))
    print(sol.hasAllCodes(s = "0110", k = 2))

if __name__ == '__main__':
    main()