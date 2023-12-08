class Solution:
    def isFascinating(self, n: int) -> bool:
        after_mod = str(n) + str(n * 2) + str(n * 3)
        res = set(after_mod)

        return not (len(res) != 9 or '0' in res or len(after_mod) != len(res))
        
        
def main():
    sol = Solution()
    print(sol.isFascinating(783))
    print(sol.isFascinating(192))
    print(sol.isFascinating(100))

if __name__ == '__main__':
    main()