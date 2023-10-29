class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        res = 0
        rounds = minutesToTest // minutesToDie

        while (rounds  + 1) ** res < buckets:
            res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.poorPigs(buckets = 4, minutesToDie = 15, minutesToTest = 15))
    print(sol.poorPigs(buckets = 4, minutesToDie = 15, minutesToTest = 30))

if __name__ == '__main__':
    main()