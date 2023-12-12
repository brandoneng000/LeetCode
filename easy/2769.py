class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t * 2)
        
def main():
    sol = Solution()
    print(sol.theMaximumAchievableX(num = 4, t = 1))
    print(sol.theMaximumAchievableX(num = 3, t = 2))

if __name__ == '__main__':
    main()