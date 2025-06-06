from collections import deque, Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        stack = []
        res = []
        min_char = 'a'

        for c in s:
            stack.append(c)
            count[c] -= 1

            while min_char != 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            
            while stack and stack[-1] <= min_char:
                res.append(stack.pop())
            
        return ''.join(res)


    # def robotWithString(self, s: str) -> str:
    #     count = Counter(s)
    #     res = []
    #     stack = []

    #     for c in s:
    #         stack.append(c)

    #         if count[c] == 1:
    #             count.pop(c)
    #         else:
    #             count[c] -= 1

    #         while count and stack and min(count) >= stack[-1]:
    #             res.append(stack.pop())
        
    #     return ''.join(res + stack[::-1])
        
    # def robotWithString(self, s: str) -> str:
    #     s_queue = deque(list(s))
    #     min_letter = min(s_queue)
    #     res = []
    #     stack = []

    #     while s_queue:
    #         if min_letter not in s_queue:
    #             min_letter = min(s_queue)
    #             while stack and min_letter >= stack[-1]:
    #                 res.append(stack.pop())
            
    #         cur = s_queue.popleft()
    #         if cur == min_letter:
    #             res.append(cur)
    #         else:
    #             stack.append(cur)
        
    #     return ''.join(res + stack[::-1])


def main():
    sol = Solution()
    print(sol.robotWithString("vzhofnpo"))
    print(sol.robotWithString("bydizfve"))
    print(sol.robotWithString("zza"))
    print(sol.robotWithString("bac"))
    print(sol.robotWithString("bdda"))

if __name__ == '__main__':
    main()