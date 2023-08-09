from typing import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, cur_word, index = [], "", 0

        for letter in searchWord:
            cur_word += letter
            index = bisect.bisect_left(products, cur_word, index)
            res.append([word for word in products[index: index + 3] if word.startswith(cur_word)])
        
        return res

    # def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    #     cur_word = ""
    #     res = []
    #     products_set = set(products)

    #     for letter in searchWord:
    #         cur_word += letter
    #         cur_search = []
    #         remove_set = set()
            
    #         for word in sorted(products_set):
    #             if word.startswith(cur_word):
    #                 if len(cur_search) < 3:
    #                     cur_search.append(word)
    #             else:
    #                 remove_set.add(word)
    #         products_set -= remove_set
    #         res.append(cur_search.copy())
        
    #     return res
        


def main():
    sol = Solution()
    print(sol.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))
    print(sol.suggestedProducts(products = ["havana"], searchWord = "havana"))

if __name__ == '__main__':
    main()