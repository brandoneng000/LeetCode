class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        smallest = min(map(len, [s1, s2, s3]))
        
        for i in range(smallest):
            if s1[i] == s2[i] == s3[i]:
                continue

            if i == 0:
                return -1
        
            return sum(len(s) - i for s in [s1, s2, s3])
        
        return sum(len(s) - smallest for s in [s1, s2, s3])
        
        
def main():
    sol = Solution()
    print(sol.findMinimumOperations(s1 = "oby", s2 = "obz", s3 = "obf"))
    print(sol.findMinimumOperations(s1 = "abc", s2 = "abb", s3 = "ab"))
    print(sol.findMinimumOperations(s1 = "dac", s2 = "bac", s3 = "cac"))

if __name__ == '__main__':
    main()