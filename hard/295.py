import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)
        
    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small, -num)
        elif not self.large:
            temp = -heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, temp)
        elif len(self.small) > len(self.large):
            temp = -heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, temp)
        else:
            temp = heapq.heappushpop(self.large, num)
            heapq.heappush(self.small, -temp)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            small = -heapq.heappop(self.small)
            heapq.heappush(self.small, -small)
            return small
        else:
            small = -heapq.heappop(self.small)
            heapq.heappush(self.small, -small)
            large = heapq.heappop(self.large)
            heapq.heappush(self.large, large)
            return (large + small) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
def main():
    # test1()
    # test2()
    test3()

def test3():
    medianFinder = MedianFinder()
    medianFinder.addNum(-1)    
    print(medianFinder.findMedian())
    medianFinder.addNum(-2)    
    print(medianFinder.findMedian())
    medianFinder.addNum(-3)    
    print(medianFinder.findMedian())
    medianFinder.addNum(-4)    
    print(medianFinder.findMedian())
    medianFinder.addNum(-5)    
    print(medianFinder.findMedian())


def test1():
    medianFinder = MedianFinder()
    medianFinder.addNum(1)    
    medianFinder.addNum(2)    
    print(medianFinder.findMedian())
    medianFinder.addNum(3)    
    print(medianFinder.findMedian())
    medianFinder.addNum(10)    
    medianFinder.addNum(11)    
    medianFinder.addNum(5)    
    medianFinder.addNum(78)    
    medianFinder.addNum(4)    
    medianFinder.addNum(9)    
    medianFinder.addNum(3)    
    medianFinder.addNum(2)    

def test2():
    medianFinder = MedianFinder()
    medianFinder.addNum(1021)    
    print(medianFinder.findMedian())
    medianFinder.addNum(9540)    
    print(medianFinder.findMedian())
    medianFinder.addNum(7788)    
    print(medianFinder.findMedian())

if __name__ == '__main__':
    main()