class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])
        # words = s.split()
        # return "".join([word[::-1] + " " for word in words])[:-1]
        
def main():
    sol = Solution()
    print(sol.reverseWords("Let's take LeetCode contest"))

if __name__ == '__main__':
    main()