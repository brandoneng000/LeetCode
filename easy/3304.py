class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ["a"]

        while len(word) < k:
            generate_string = word.copy()

            for i in range(len(word)):
                generate_string[i] = chr(((ord(generate_string[i]) - ord('a') + 1) % 26) + ord('a'))
            
            word.extend(generate_string)
        
        return word[k - 1]
        
def main():
    sol = Solution()
    print(sol.kthCharacter(5))
    print(sol.kthCharacter(10))

if __name__ == '__main__':
    main()