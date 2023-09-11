import collections

class UndergroundSystem:

    def __init__(self):
        self.id = {}
        self.travel_time = collections.defaultdict(int)
        self.trips = collections.defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.id and self.id[id] != (-1, ""):
            return
        self.id[id] = (t, stationName)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, start_station = self.id[id]

        if start_time == -1:
            return
        
        self.travel_time[start_station, stationName] += t - start_time
        self.trips[start_station, stationName] += 1
        self.id[id] = (-1, "")
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travel_time[startStation, endStation] / self.trips[startStation, endStation]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)