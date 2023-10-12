import collections

class Solution:
    def numSplits(self, s: str) -> int:
        left = set()
        right = collections.Counter(s)
        res = 0

        for i in range(len(s) - 1):
            left.add(s[i])
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            
            res += len(left) == len(right)
        
        return res

def main():
    sol = Solution()
    print(sol.numSplits("aacaba"))
    print(sol.numSplits("abcd"))

if __name__ == '__main__':
    main()        