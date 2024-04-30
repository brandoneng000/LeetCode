class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        discount = 1 - (discount / 100)
        words = sentence.split()

        for i in range(len(words)):
            if words[i][0] == '$' and words[i][1:].isdigit():
                words[i] = '$' + '{:.2f}'.format(float(words[i][1:]) * discount)
        
        return ' '.join(words)
        
def main():
    sol = Solution()
    print(sol.discountPrices(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 36))
    print(sol.discountPrices(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50))
    print(sol.discountPrices(sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100))

if __name__ == '__main__':
    main()