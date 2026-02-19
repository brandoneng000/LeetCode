class Solution:
    # def countBinarySubstrings(self, s: str) -> int:
    #     n = len(s)
    #     groups = [1]
    #     res = 0

    #     for i in range(1, n):
    #         if s[i] != s[i - 1]:
    #             groups.append(1)
    #         else:
    #             groups[-1] += 1

        
    #     for i in range(1, len(groups)):
    #         res += min(groups[i], groups[i - 1])
        
    #     return res

    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        cur = 1
        count = 0

        for index in range(1, len(s)):
            if s[index-1] != s[index]:
                count += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        count += min(prev, cur)
        return count

        
def main():
    sol = Solution()
    print(sol.countBinarySubstrings("00110011"))
    print(sol.countBinarySubstrings("10101"))

if __name__ == '__main__':
    main()