from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        current = ord('a')

        for i in range(n):
            if not word[i]:
                if current > ord('z'):
                    return ""
                word[i] = chr(current)

                for j in range(i + 1, n):
                    if lcp[i][j]:
                        word[j] = word[i]
                current += 1
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j]:
                        return ""
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
        
        return ''.join(word)
                
        
def main():
    sol = Solution()
    print(sol.findTheString([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]))
    print(sol.findTheString([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]))
    print(sol.findTheString([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]))

if __name__ == '__main__':
    main()