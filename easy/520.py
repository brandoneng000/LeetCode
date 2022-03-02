
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        from string import ascii_uppercase as upper

        for index, letter in enumerate(word):
            if index == 0:
                pass
            elif letter in upper and word[index - 1] not in upper:
                return False
            elif letter not in upper:
                if index - 1 > 0:
                    return False
                while index < len(word):
                    if word[index] in upper:
                        return False
                    index += 1
                break

        return True
        
def main():
    sol = Solution()
    print(sol.detectCapitalUse("USA"))
    print(sol.detectCapitalUse("Google"))
    print(sol.detectCapitalUse("FlaG"))
    print(sol.detectCapitalUse("Flaserhyojsernoingaeornhgyseoiurybhbiuearsbyhbsiurthbs"))
    print(sol.detectCapitalUse("FlaserhyojsernoingaeornhgyseoiurybhbiuearsbyhbsiurthbsD"))
    print(sol.detectCapitalUse("mL"))
    

if __name__ == '__main__':
    main()