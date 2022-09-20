class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

        
def main():
    sol = Solution()
    print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
    print(sol.checkIfPangram("leetcode"))

if __name__ == '__main__':
    main()