class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        
        for index, letter in enumerate(s):
            if letter not in char_dict:
                char_dict[letter] = index
            else:
                char_dict[letter] = 1000000

        return min(char_dict.values()) if min(char_dict.values()) != 1000000 else -1
        
def main():
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))
    print(sol.firstUniqChar("loveleetcode"))
    print(sol.firstUniqChar("aabb"))
    print(sol.firstUniqChar("aadadaad"))

if __name__ == '__main__':
    main()