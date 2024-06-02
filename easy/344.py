from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)

        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]

    # def reverseString(self, s: List[str]) -> None:
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
    #     size = len(s) // 2
    #     index = 0
        
    #     while index < size:
    #         temp = s[index]
    #         s[index] = s[len(s) - index - 1]
    #         s[len(s) - index - 1] = temp
    #         index += 1


def main():
    sol = Solution()
    s = ["h","e","l","l","o"]
    sol.reverseString(s)
    print(s)
    s = ["H","a","n","n","a","h"]
    sol.reverseString(s)
    print(s)

if __name__ == '__main__':
    main()