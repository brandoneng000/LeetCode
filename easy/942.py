from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = 0
        end = len(s)
        result = []

        for letter in s:
            if letter == "I":
                result.append(start)
                start += 1
            elif letter == "D":
                result.append(end)
                end -= 1
        
        result.append(end)
        return result

def main():
    sol = Solution()
    print(sol.diStringMatch("IDID"))
    print(sol.diStringMatch("III"))
    print(sol.diStringMatch("DDI"))

if __name__ == '__main__':
    main()