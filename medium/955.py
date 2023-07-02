from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:     
        m, n = len(strs), len(strs[0])
        res = 0
        ordered = [False] * (m - 1)

        for j in range(n):
            temp = ordered.copy()
            for i in range(m - 1):
                if not ordered[i] and strs[i][j] > strs[i + 1][j]:
                    res += 1
                    break
                elif strs[i][j] < strs[i + 1][j] and not ordered[i]:
                    temp[i] = True
            else:
                ordered = temp
            if all(ordered):
                return res
        return res
        

def main():
    sol = Solution()
    print(sol.minDeletionSize(["vdy","vei","zvc","zld"]))
    print(sol.minDeletionSize(["xga","xfb","yfa"]))
    print(sol.minDeletionSize(["jwkwdc","etukoz"]))
    print(sol.minDeletionSize(["ca","bb","ac"]))
    print(sol.minDeletionSize(["xc","yb","za"]))
    print(sol.minDeletionSize(["zyx","wvu","tsr"]))

if __name__ == '__main__':
    main()