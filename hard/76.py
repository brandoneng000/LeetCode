from collections import Counter

class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     def check_letters(window: str) -> bool:
    #         for char in t:
    #             if t.count(char) > window.count(char):
    #                 return False
    #         return True
        
    #     if not check_letters(s):
    #         return ""
        
    #     start, end = 0, len(t) - 1
    #     index = 0
    #     res = s

    #     while end < len(s) + 1:
    #         window = s[start: end]
    #         if not check_letters(window):
    #             end += 1
    #         else:
    #             while check_letters(window):
    #                 if len(res) > len(window):
    #                     res = window
    #                 start += 1
    #                 window = s[start: end]
                
    #     return res        
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        unique_chars = len(dict_t)
        start, end = 0, 0
        formed = 0
        count_window = {}
        res = float("inf"), start, end

        while end < len(s):
            char = s[end]
            count_window[char] = count_window.get(char, 0) + 1

            if char in dict_t and count_window[char] == dict_t[char]:
                formed += 1
            
            while start <= end and formed == unique_chars:
                char = s[start]

                if end - start + 1 < res[0]:
                    res = (end - start + 1, start, end)

                count_window[char] -= 1
                if char in dict_t and count_window[char] < dict_t[char]:
                    formed -= 1
                
                start += 1
            end += 1
        
        return "" if res[0] == float("inf") else s[res[1] : res[2] + 1]

def main():
    sol = Solution()
    # print(sol.minWindow("ADOBECODEBANC", "ABC"))
    print(sol.minWindow("aa", "aa"))

if __name__ == '__main__':
    main()