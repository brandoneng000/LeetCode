import collections

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))

        if k > total:
            return ""
        
        res = ["a"] * n

        next_smallest = { "a": "b", "b": "a", "c": "a" }
        next_greatest = { "a": "c", "b": "c", "c": "b" }

        start_a = 1
        start_b = start_a + (1 << (n - 1))
        start_c = start_b + (1 << (n - 1))

        if k < start_b:
            res[0] = "a"
            k -= start_a
        elif k < start_c:
            res[0] = "b"
            k -= start_b
        else:
            res[0] = "c"
            k -= start_c

        for index in range(1, n):
            middle = 1 << (n - index - 1)

            if k < middle:
                res[index] = next_smallest[res[index - 1]]
            else:
                res[index] = next_greatest[res[index - 1]]
                k -= middle
        
        return ''.join(res)


    # def getHappyString(self, n: int, k: int) -> str:
    #     q = collections.deque(['a', 'b', 'c'])
    #     happy = ['a', 'b', 'c']
    #     happy_strings = []

    #     while q:
    #         cur = q.popleft()

    #         if len(cur) == n:
    #             happy_strings.append(cur)
    #             continue

    #         for letter in happy:
    #             if cur[-1] != letter:
    #                 q.append(cur + letter)
        
    #     if len(happy_strings) < k:
    #         return ""
    #     else:
    #         return happy_strings[k - 1]


        
def main():
    sol = Solution()
    print(sol.getHappyString(n = 1, k = 3))
    print(sol.getHappyString(n = 1, k = 4))
    print(sol.getHappyString(n = 3, k = 9))

if __name__ == '__main__':
    main()