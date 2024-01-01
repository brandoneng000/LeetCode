from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookies = sorted(s)
        greed = sorted(g)
        c = k = 0

        while c < len(cookies) and k < len(greed):
            if cookies[c] >= greed[k]:
                k += 1
            c += 1
        
        return k

    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     if s:
    #         s.sort()
    #     else:
    #         return 0

    #     g.sort()
    #     content = 0

    #     for cookie in s:
    #         if g[content] <= cookie:
    #             content += 1
    #             if content == len(g):
    #                 break
        
    #     return content
        
        # content = 0

        # while len(s) > 0 and len(g) > 0:
        #     if min(g) > max(s):
        #         break
        #     greediest = max(g)
        #     cookie = max(s)

        #     if greediest <= cookie:
        #         s.remove(cookie)
        #         g.remove(greediest)
        #         content += 1
        #     elif greediest > cookie:
        #         g.remove(greediest)
            
        # return content
        

def main():
    sol = Solution()
    print(sol.findContentChildren([1,2,3], [1,1]))
    print(sol.findContentChildren([1,2], [1,2,3]))

if __name__ == '__main__':
    main()