from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix = [0]
        last_metal = last_glass = last_paper = 0
        res = 0

        for i in range(len(travel)):
            prefix.append(prefix[-1] + travel[i])
        
        for i, g in enumerate(garbage):
            res += len(g)
            if 'M' in g:
                last_metal = i
            if 'G' in g:
                last_glass = i
            if 'P' in g:
                last_paper = i
        
        return res + prefix[last_metal] + prefix[last_glass] + prefix[last_paper]


def main():
    sol = Solution()
    print(sol.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3]))
    print(sol.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))

if __name__ == '__main__':
    main()