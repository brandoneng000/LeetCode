from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        len_a, len_b = len(a), len(b)
        list_a = []
        list_b = []
        res = []

        for i in range(n):
            if s[i: i + len_a] == a:
                list_a.append(i)
            
            if s[i: i + len_b] == b:
                list_b.append(i)
        
        for i in list_a:
            for j in list_b:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        
        return res

        
def main():
    sol = Solution()
    print(sol.beautifulIndices(s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15))
    print(sol.beautifulIndices(s = "abcd", a = "a", b = "a", k = 4))

if __name__ == '__main__':
    main()