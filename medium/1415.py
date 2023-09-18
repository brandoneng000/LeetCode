import collections

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        q = collections.deque(['a', 'b', 'c'])
        happy = ['a', 'b', 'c']
        happy_strings = []

        while q:
            cur = q.popleft()

            if len(cur) == n:
                happy_strings.append(cur)
                continue

            for letter in happy:
                if cur[-1] != letter:
                    q.append(cur + letter)
        
        if len(happy_strings) < k:
            return ""
        else:
            return happy_strings[k - 1]


        
def main():
    sol = Solution()
    print(sol.getHappyString(n = 1, k = 3))
    print(sol.getHappyString(n = 1, k = 4))
    print(sol.getHappyString(n = 3, k = 9))

if __name__ == '__main__':
    main()