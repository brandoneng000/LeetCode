from collections import deque, Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        res = ""
        candidates = sorted([c for c, w in Counter(s).items() if w >= k], reverse=True)
        q = deque(candidates)

        while q:
            cur = q.popleft()

            if len(cur) > len(res):
                res = cur

            for char in candidates:
                nxt = cur + char
                it = iter(s)

                if all(char in it for char in nxt * k):
                    q.append(nxt)
            
        return res


def main():
    sol = Solution()
    print(sol.longestSubsequenceRepeatedK(s = "letsleetcode", k = 2))
    print(sol.longestSubsequenceRepeatedK(s = "bb", k = 2))
    print(sol.longestSubsequenceRepeatedK(s = "ab", k = 2))

if __name__ == '__main__':
    main()