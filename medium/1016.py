class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for num in range(1, n + 1):
            if format(num, 'b') not in s:
                return False
        
        return True

def main():
    sol = Solution()
    print(sol.queryString(s = "0110", n = 3))
    print(sol.queryString(s = "0110", n = 4))

if __name__ == '__main__':
    main()