from collections import defaultdict

class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.memory = [-1] * n
        self.mID_indexes = defaultdict(list)
    
    def allocate(self, size: int, mID: int) -> int:
        free = index = 0
        
        for i in range(self.n):
            if free == 0:
                index = i
            if self.memory[i] == -1:
                free += 1
            else:
                free = 0
            
            if free == size:
                break
        
        if free == size:
            for i in range(index, index + size):
                self.memory[i] = mID
                self.mID_indexes[mID].append(i)

            return index

        return -1


    def free(self, mID: int) -> int:
        for i in self.mID_indexes[mID]:
            self.memory[i] = -1

        return len(self.mID_indexes.pop(mID))
        
            
            


        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)