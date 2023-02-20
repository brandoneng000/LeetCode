class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = {}
        self.parking[1] = big
        self.parking[2] = medium
        self.parking[3] = small
        

    def addCar(self, carType: int) -> bool:
        if self.parking[carType] > 0:
            self.parking[carType] -= 1
            return True
        return False