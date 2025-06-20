class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        latitude = longitude = 0

        for i in range(n):
            if s[i] == 'N':
                latitude += 1
            elif s[i] == 'S':
                latitude -= 1
            elif s[i] == 'E':
                longitude += 1
            elif s[i] == 'W':
                longitude -= 1
            res = max(res, min(abs(latitude) + abs(longitude) + k * 2, i + 1))

        return res



        
def main():
    sol = Solution()
    print(sol.maxDistance(s = "EWWE", k = 0))
    print(sol.maxDistance(s = "NWSE", k = 1))
    print(sol.maxDistance(s = "NSWWEW", k = 3))

if __name__ == '__main__':
    main()