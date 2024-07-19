from collections import Counter

class FrequencyTracker:

    def __init__(self):
        self.count = Counter()
        self.freq = Counter()

    def add(self, number: int) -> None:
        self.freq[self.count[number]] -= 1
        self.count[number] += 1
        self.freq[self.count[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.count[number] > 0:
            self.freq[self.count[number]] -= 1
            self.count[number] -= 1
            self.freq[self.count[number]] += 1


    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)