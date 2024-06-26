class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_log = {}
        t_log = {}

        for x, y in zip(s, t):
            if x in s_log and y in t_log:
                if s_log[x] != y:
                    return False
            elif x in s_log or y in t_log:
                return False
            else:
                s_log[x] = y
                t_log[y] = x
        
        return True
        

    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     word_dict = {}

    #     for letter in range(len(s)):
    #         if s[letter] not in word_dict.keys() and t[letter] not in word_dict.values():
    #             word_dict[s[letter]] = t[letter]
    #         else:
    #             if s[letter] not in word_dict.keys():
    #                 return False
    #             if word_dict[s[letter]] != t[letter]:
    #                 return False
                    
    #     return True

        # word_dict = {}
        # reverse_dict = {}

        # for letter in range(len(s)):
        #     if s[letter] not in word_dict.keys() and t[letter] not in reverse_dict.keys():
        #         word_dict[s[letter]] = t[letter]
        #         reverse_dict[t[letter]] = s[letter]
        #     else:
        #         if s[letter] not in word_dict.keys() or t[letter] not in reverse_dict.keys():
        #             return False
        #         if word_dict[s[letter]] != t[letter] or reverse_dict[t[letter]] != s[letter]:
        #             return False

        # return True
        
def main():
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))
    print(sol.isIsomorphic("foo", "bar"))
    print(sol.isIsomorphic("paper", "title"))
    print(sol.isIsomorphic("badc", "baba"))

if __name__ == "__main__":
    main()