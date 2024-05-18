class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        res = 0

        while '01' in s:
            s = s.replace('01', '10')
            res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.secondsToRemoveOccurrences("0110101"))
    print(sol.secondsToRemoveOccurrences("11100"))

if __name__ == '__main__':
    main()