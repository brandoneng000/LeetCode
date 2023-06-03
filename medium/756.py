from typing import List
import collections
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        triangles = collections.defaultdict(list)

        for tri in allowed:
            triangles[tri[:2]].append(tri[2])
        
        def helper(level: str):
            if len(level) == 2:
                return level in triangles
            cur_level_tri = collections.deque([''])
            temp = collections.deque()
            for i in range(len(level) - 1):
                cur_tri = level[i: i + 2]
                if cur_tri not in triangles:
                    return False
                temp = collections.deque()
                for tri in cur_level_tri:
                    for color in triangles[cur_tri]:
                        temp.append(tri + color)
                cur_level_tri = temp
            
            for test_level in cur_level_tri:
                if helper(test_level):
                    return True
            return False
        
        return helper(bottom)





def main():
    sol = Solution()
    print(sol.pyramidTransition(bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]))
    print(sol.pyramidTransition(bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]))

if __name__ == '__main__':
    main()