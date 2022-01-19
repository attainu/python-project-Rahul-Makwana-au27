from function import Parking_Lot


class File:
    def __init__(self):
        self.obj = Parking_Lot()

    def Create_Parking(self, row):
        user_input = list(row.split())
        size = int(user_input[1])
        self.obj.CreateParkingLot(size)

    def Activities(self, row):
        User_Input = row
        self.obj.Activities(User_Input)
