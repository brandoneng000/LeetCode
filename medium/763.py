from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = { c: i for i, c in enumerate(s) }
        left = right = 0
        res = []

        for i, c in enumerate(s):
            right = max(right, last_index[c])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        
        return res

    # def partitionLabels(self, s: str) -> List[int]:
    #     found = set()
    #     res = []
    #     left, right = 0, 0
    #     while left < len(s):
    #         original_left = left
    #         right = original_left
    #         while left <= right:
    #             temp = s[left]
    #             if temp not in found:
    #                 found.add(temp)
    #                 right = max(right, s.rindex(s[left]))
    #             left += 1
    #         res.append(right - original_left + 1)

    #     return res



def main():
    sol = Solution()
    print(sol.partitionLabels("caedbdedda"))
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))
    print(sol.partitionLabels("eccbbbbdec"))

if __name__ == '__main__':
    main()