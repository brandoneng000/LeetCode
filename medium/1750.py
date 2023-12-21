from collections import deque

class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
        
        return len(s)
    
    # def minimumLength(self, s: str) -> int:
    #     string_chars = deque()
        
    #     for c in s:
    #         if not string_chars or string_chars[-1][0] != c:
    #             string_chars.append([c, 1])
    #         elif string_chars[-1][0] == c:
    #             string_chars[-1][1] += 1
        
    #     while len(string_chars) > 1 and string_chars[0][0] == string_chars[-1][0]:
    #         string_chars.popleft()
    #         string_chars.pop()
        
    #     if len(string_chars) == 1:
    #         return 1 if string_chars[0][1] == 1 else 0

    #     return sum(count for char, count in string_chars) if string_chars else 0
        



def main():
    sol = Solution()
    print(sol.minimumLength("ca"))
    print(sol.minimumLength("cabaabac"))
    print(sol.minimumLength("aabccabba"))

if __name__ == '__main__':
    main()