class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        result = []

        for word in words:
            word = word.lower()
            if len(word) < 3:
                result.append(word)
            else:
                result.append(word[0].capitalize() + word[1:])

        return " ".join(result)
        
def main():
    sol = Solution()
    print(sol.capitalizeTitle("capiTalIze tHe titLe"))

if __name__ == '__main__':
    main()