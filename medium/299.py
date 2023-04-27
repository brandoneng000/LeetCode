import collections

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = 0
        bulls = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        
        secret_counter = collections.Counter(secret)
        guess_counter = collections.Counter(guess)
        cows = sum(secret_counter.values()) - sum((secret_counter - guess_counter).values()) - bulls
        
        return f"{bulls}A{cows}B"

def main():
    sol = Solution()
    print(sol.getHint(secret = "1807", guess = "7810"))
    print(sol.getHint(secret = "1123", guess = "0111"))

if __name__ == '__main__':
    main()