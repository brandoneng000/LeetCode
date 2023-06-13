from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res = list(s)

        for index, source, target in zip(indices, sources, targets):
            if not s[index:].startswith(source):
                continue
            else:
                res[index] = target
                for i in range(index + 1, index + len(source)):
                    res[i] = ''
        
        return "".join(res)

def main():
    sol = Solution()
    print(sol.findReplaceString(s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]))
    print(sol.findReplaceString(s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]))

if __name__ == '__main__':
    main()