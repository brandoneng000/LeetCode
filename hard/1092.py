class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        prev_row = [str2[0:col] for col in range(m + 1)]

        for row in range(1, n + 1):
            cur_row = [str1[0:row]] + [None for _ in range(m)]

            for col in range(1, m + 1):
                if str1[row - 1] == str2[col - 1]:
                    cur_row[col] = prev_row[col - 1] + str1[row - 1]
                else:
                    pick_s1 = prev_row[col]
                    pick_s2 = cur_row[col - 1]

                    cur_row[col] = (
                        pick_s1 + str1[row - 1]
                        if len(pick_s1) < len(pick_s2)
                        else pick_s2 + str2[col - 1]
                    )
            prev_row = cur_row
        
        return prev_row[m]
        
def main():
    sol = Solution()
    print(sol.shortestCommonSupersequence(str1 = "abac", str2 = "cab"))
    print(sol.shortestCommonSupersequence(str1 = "aaaaaaaa", str2 = "aaaaaaaa"))

if __name__ == '__main__':
    main()