class Solution:
    def addMinimum(self, word: str) -> int:
        word = word.replace('abc', '0')

        for w in ['ab', 'bc', 'ac']:
            word = word.replace(w, '1')
        
        for w in 'abc':
            word = word.replace(w, '2')
        
        return sum(int(val) for val in word)
        
def main():
    sol = Solution()
    print(sol.addMinimum("b"))
    print(sol.addMinimum("aaa"))
    print(sol.addMinimum("abc"))

if __name__ == '__main__':
    main()