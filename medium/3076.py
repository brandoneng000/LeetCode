from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        res = [""] * n

        for i in range(n):
            for size in range(1, len(arr[i]) + 1):
                for j in range(len(arr[i]) - size + 1):
                    cur = arr[i][j: j + size]

                    for k in range(n):
                        if i == k:
                            continue
                        
                        if cur in arr[k]:
                            break
                    else:
                        res[i] = min(res[i], cur) if res[i] != "" else cur
                    
                if res[i] != "":
                    break

        return res

def main():
    sol = Solution()
    print(sol.shortestSubstrings(["tqnf","wrb","uke","d","eq","nuhyo"]))
    print(sol.shortestSubstrings(["vbb","grg","lexn","oklqe","yxav"]))
    print(sol.shortestSubstrings(["cab","ad","bad","c"]))
    print(sol.shortestSubstrings(["abc","bcd","abcd"]))

if __name__ == '__main__':
    main()