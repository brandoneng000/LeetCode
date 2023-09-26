import heapq

class Solution:
    def arrangeWords(self, text: str) -> str:
        return " ".join(sorted(text.split(), key=len)).capitalize()
    
    # def arrangeWords(self, text: str) -> str:
    #     heap = []
    #     res = []

    #     for i, word in enumerate(text.split()):
    #         heapq.heappush(heap, (len(word), i, word.lower()))
        
    #     while heap:
    #         size, index, word = heapq.heappop(heap)

    #         res.append(word)
        
    #     return " ".join(res).capitalize()

        
def main():
    sol = Solution()
    print(sol.arrangeWords("Leetcode is cool"))
    print(sol.arrangeWords("Keep calm and code on"))
    print(sol.arrangeWords("To be or not to be"))

if __name__ == '__main__':
    main()