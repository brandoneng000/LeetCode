class Solution:
    def makeFancyString(self, s: str) -> str:
        from string import ascii_lowercase
        triplets = []
        for letter in ascii_lowercase:
            triplets.append(letter * 3)

        for triple in triplets:
            while triple in s:
                s = s.replace(triple, triple[:2])
        
        return s


def main():
    sol = Solution()
    print(sol.makeFancyString("leeetcode"))
    print(sol.makeFancyString("aaabaaaa"))
    print(sol.makeFancyString("aab"))

if __name__ == '__main__':
    main()