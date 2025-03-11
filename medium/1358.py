import collections

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        prev_index = [-1] * 3
        res = 0

        for i in range(n):
            prev_index[ord(s[i]) - ord('a')] = i
            res += 1 + min(prev_index)
        
        return res


    # def numberOfSubstrings(self, s: str) -> int:
    #     res = 0
    #     n = len(s)
    #     count = collections.Counter()
    #     left = 0

    #     for right in range(n):
    #         count[s[right]] += 1

    #         if len(count) == 3:
    #             while len(count) == 3:
    #                 count[s[left]] -= 1
    #                 if count[s[left]] == 0:
    #                     count.pop(s[left])
    #                 left += 1
                
    #                 res += n - right
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.numberOfSubstrings("acbbcac"))
    print(sol.numberOfSubstrings("abcabc"))
    print(sol.numberOfSubstrings("aaacb"))
    print(sol.numberOfSubstrings("abc"))

if __name__ == '__main__':
    main()