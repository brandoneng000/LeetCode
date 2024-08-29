class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        def helper(i: int):
            if i == 0:
                return x / 2
            if i == -1:
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = min(helper(i - 1) + x / 2, helper(i - 2) + differences[i] - differences[i - 1])
            return cache[i]


        n = len(s1)
        differences = []
        cache = {}
        
        for i in range(n):
            if s1[i] != s2[i]:
                differences.append(i)

        if len(differences) % 2 == 1:
            return -1
        
        return int(helper(len(differences) - 1))
        
def main():
    sol = Solution()
    print(sol.minOperations(s1 = "1100011000", s2 = "0101001010", x = 2))
    print(sol.minOperations(s1 = "10110", s2 = "00011", x = 4))

if __name__ == '__main__':
    main()