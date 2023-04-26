from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        # return max(list(map(lambda x: int(x) if x.isdecimal() else len(x), strs)))
        return max(int(s) if s.isdecimal() else len(s) for s in strs)


def main():
    sol = Solution()
    print(sol.maximumValue(["alic3","bob","3","4","00000"]))
    print(sol.maximumValue(["1","01","001","0001"]))

if __name__ == '__main__':
    main()