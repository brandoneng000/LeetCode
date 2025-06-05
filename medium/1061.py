import string
from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def dfs(letter: str, visited: set):
            visited.add(letter)
            min_char = letter

            for nei in letters[letter]:
                if nei not in visited:
                    candidate = dfs(nei, visited)
                    min_char = min(min_char, candidate)
            
            return min_char

        letters = defaultdict(list)
        cache = {}

        for a, b in zip(s1, s2):
            letters[a].append(b)
            letters[b].append(a)
        
        for letter in string.ascii_lowercase:
            visited = set()
            cache[letter] = dfs(letter, visited)
        
        return ''.join(cache[letter] for letter in baseStr)

    # def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    #     def find(letter: str):
    #         if letter != data[letter]:
    #             data[letter] = find(data[letter])
    #         return data[letter]

    #     data = { a: a for a in string.ascii_lowercase }

    #     for l1, l2 in zip(s1, s2):
    #         key1, key2 = find(l1), find(l2)
    #         data[key1] = data[key2] = min(key1, key2)
                
    #     return "".join(find(letter) for letter in baseStr)


def main():
    sol = Solution()
    print(sol.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser"))
    print(sol.smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold"))
    print(sol.smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"))

if __name__ == '__main__':
    main()