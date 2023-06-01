class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.double = []

    def book(self, start: int, end: int) -> bool:
        for cur_start, cur_end in self.double:
            if cur_start < end and start < cur_end:
                return False
        for cur_start, cur_end in self.bookings:
            if cur_start < end and start < cur_end:
                self.double.append((max(start, cur_start), min(end, cur_end)))
        self.bookings.append([start, end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)