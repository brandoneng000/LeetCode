import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        s_count = collections.Counter(s)
        sorted_s = sorted(set(s), key=lambda x: s_count[x], reverse=True)
        res = []
        for s in sorted_s:
            res.extend([s] * s_count[s])

        return "".join(res)

        # s_count = collections.Counter(s)
        # sorted_s = sorted(s, key=lambda x: (s_count[x], x), reverse=True)
        
        # return "".join(sorted_s)

def main():
    sol = Solution()
    print(sol.frequencySort("tree"))
    print(sol.frequencySort("cccaaa"))
    print(sol.frequencySort("Aabb"))
    print(sol.frequencySort("loveleetcode"))

if __name__ == '__main__':
    main()