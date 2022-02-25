from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0

        while len(s) > 0 and len(g) > 0:
            if min(g) > max(s):
                break
            greediest = max(g)
            cookie = max(s)

            if greediest <= cookie:
                s.remove(cookie)
                g.remove(greediest)
                content += 1
            elif greediest > cookie:
                g.remove(greediest)
            
        return content
        

def main():
    sol = Solution()
    print(sol.findContentChildren([1,2,3], [1,1]))
    print(sol.findContentChildren([1,2], [1,2,3]))

if __name__ == '__main__':
    main()