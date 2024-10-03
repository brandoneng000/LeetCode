class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        res = 1
        cur = word[k:]

        while not word.startswith(cur):
            res += 1

            if len(cur) < k:
                break
            else:
                cur = cur[k:]
        
        return res
        
def main():
    sol = Solution()
    print(sol.minimumTimeToInitialState(word = "abacaba", k = 3))
    print(sol.minimumTimeToInitialState(word = "abacaba", k = 4))
    print(sol.minimumTimeToInitialState(word = "abcbabcd", k = 2))

if __name__ == '__main__':
    main()