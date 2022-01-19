from function import Parking_Lot


class Interactive:
    def __init__(self):

        self.obj = Parking_Lot()

    def Create_Parking(self):
        User_Input = list(input("Create parking lot :").split())
        size = int(User_Input[1])
        self.obj.CreateParkingLot(size)

    def Activities(self):
        temp = "true"
        while temp == "true":
            User_Input = input()
            if User_Input == "exit":
                temp = "false"
                break
            else:
                self.obj.Activities(User_Input)
