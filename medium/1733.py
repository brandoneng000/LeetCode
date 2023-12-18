from typing import List
from collections import Counter

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages_spoke = [set(l) for l in languages]

        teach = set()

        for x, y in friendships:
            x -= 1
            y -= 1
            if languages_spoke[x] & languages_spoke[y]:
                continue
            teach.add(x)
            teach.add(y)
        
        language_count = Counter()
        for f in teach:
            for l in languages_spoke[f]:
                language_count[l] += 1
        
        return 0 if not teach else len(teach) - max(language_count.values())


def main():
    sol = Solution()
    print(sol.minimumTeachings(n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]))
    print(sol.minimumTeachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]))

if __name__ == '__main__':
    main()