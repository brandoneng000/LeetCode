from typing import List

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        INF = 10 ** 33
        n = len(words)
        res = INF

        for i in range(n):
            if words[i] == target:
                res = min(res, abs(i - startIndex), n - abs(i - startIndex))
            
        return res if res != INF else -1


    # def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
    #     if target not in words:
    #         return -1
    #     forward = backward = startIndex
    #     count = 0
    #     while words[forward] != target and words[backward] != target:
    #         count += 1
    #         forward += 1
    #         backward -= 1
    #         if forward == len(words):
    #             forward = 0
    #         if backward == -(len(words) + 1):
    #             backward = len(words) - 1
            
    #     return count
        

def main():
    sol = Solution()
    print(sol.closetTarget(words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1))
    print(sol.closetTarget(words = ["a","b","leetcode"], target = "leetcode", startIndex = 0))
    print(sol.closetTarget(words = ["i","eat","leetcode"], target = "ate", startIndex = 0))

if __name__ == '__main__':
    main()