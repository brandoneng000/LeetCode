class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for index in range(len(pattern)):
            if words[index] in patterns.values():
                if pattern[index] not in patterns or patterns[pattern[index]] != words[index]:
                    return False
            elif pattern[index] not in patterns:
                patterns[pattern[index]] = words[index]
            elif patterns[pattern[index]] != words[index]:
                return False

        return True
        
def main():
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))
    print(sol.wordPattern("abba", "dog cat cat fish"))
    print(sol.wordPattern("abba", "dog dog dog dog"))
    print(sol.wordPattern("aaaa", "dog cat cat dog"))

if __name__ == '__main__':
    main()