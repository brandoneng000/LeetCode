class RecentCounter:

    def __init__(self):
        self.incoming_req = []

    def ping(self, t: int) -> int:
        timer = t - 3000
        remove = 0
        
        for index in range(len(self.incoming_req)):
            if timer > self.incoming_req[index]:
                remove += 1
            else:
                break
        
        while remove > 0:
            remove -= 1
            self.incoming_req.pop(0)

        self.incoming_req.append(t)
        return len(self.incoming_req)
        
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
def main():
    sol = RecentCounter()
    print(sol.ping(1))
    print(sol.ping(100))
    print(sol.ping(3001))
    print(sol.ping(3002))

if __name__ == '__main__':
    main()