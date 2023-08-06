from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = []

        for s in arr:
            u = set(s)
            if len(u) == len(s):
                unique.append(u)
        
        concat = [set()]

        for u in unique:
            for c in concat:
                if not c & u:
                    concat.append(c | u)
        
        return max(len(c) for c in concat)

    # def maxLength(self, arr: List[str]) -> int:
    #     def helper(cur: List[str], used: set, size: int, index: int):
    #         if len(cur) == size:
    #             self.res = max(self.res, len("".join(cur)))
    #             return
            
    #         for i in range(index, len(arr)):
    #             if all(letter not in used for letter in arr[i]) and len(arr[i]) == len(set(arr[i])):
    #                 cur.append(arr[i])
    #                 used.update(arr[i])
    #                 helper(cur, used, size, i + 1)
    #                 cur.pop()
    #                 used.difference_update(arr[i])
        
    #     self.res = 0

    #     for size in range(1, len(arr) + 1):
    #         helper([], set(), size, 0)
        
    #     return self.res


def main():
    sol = Solution()
    print(sol.maxLength(["un","iq","ue"]))
    print(sol.maxLength(["cha","r","act","ers"]))
    print(sol.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
    print(sol.maxLength(["aa"]))

if __name__ == '__main__':
    main()