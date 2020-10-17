# title: design-parking-system
# detail: https://leetcode.com/submissions/detail/409492316/
# datetime: Fri Oct 16 23:52:09 2020
# runtime: 136 ms
# memory: 14.6 MB

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.slots[carType - 1] -= 1
        return self.slots[carType - 1] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)