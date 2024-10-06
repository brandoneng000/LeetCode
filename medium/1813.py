from collections import deque

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        
        s1, s2 = deque(sentence1.split()), deque(sentence2.split())

        while s1 and s2 and s1[0] == s2[0]:
            s1.popleft()
            s2.popleft()

        while s1 and s2 and s1[-1] == s2[-1]:
            s1.pop()
            s2.pop()
        
        return len(s1) == 0


    # def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
    #     if len(sentence1) < len(sentence2):
    #         sentence1, sentence2 = sentence2, sentence1
        
    #     s1, s2 = sentence1.split(), sentence2.split()
    #     n, m = len(s1), len(s2)
    #     j = 0

    #     for i in range(n):
    #         if j < m and s1[i] == s2[j]:
    #             j += 1
    #         else:
    #             break
        
    #     n -= 1
    #     for j in range(m - 1, j - 1, -1):
    #         if s1[n] == s2[j]:
    #             n -= 1
    #         else:
    #             break
    #     else:
    #         return True

    #     return False
        
def main():
    sol = Solution()
    print(sol.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley"))
    print(sol.areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words"))
    print(sol.areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating"))

if __name__ == '__main__':
    main()