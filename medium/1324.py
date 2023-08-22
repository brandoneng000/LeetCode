from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_split = s.split()
        size = len(max(s_split, key=len))
        res = [[] for i in range(size)]

        for word in s_split:
            for i in range(size):
                if i < len(word):
                    res[i].append(word[i])
                else:
                    res[i].append(' ')
        
        return ["".join(res[i]).rstrip() for i in range(size)]

def main():
    sol = Solution()
    print(sol.printVertically("HOW ARE YOU"))
    print(sol.printVertically("TO BE OR NOT TO BE"))
    print(sol.printVertically("CONTEST IS COMING"))

if __name__ == '__main__':
    main()