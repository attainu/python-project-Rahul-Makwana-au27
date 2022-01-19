
from interaction import Interactive
from files import File

if __name__ == "__main__":

    print("1.interactive for manual input. 2.file for giving input in a file")
    while True:
        mode = input("write interactive or file to choose from them :")
        print()
        manual = Interactive()
        auto = File()

        if mode == "interactive":
            ctr = 0
            while ctr < 2:
                if ctr == 0:
                    manual.Create_Parking()
                    ctr += 1
                else:
                    manual.Activities()
                    ctr += 1
        elif mode == "file":
            file_address = input("file location please :")
            f = open(file_address, "r")
            ctr = 0
            for row in f:
                if ctr == 0:
                    auto.Create_Parking(row)
                    ctr += 1
                else:
                    auto.Activities(row)
        elif mode == "exit":
            break
        else:
            print("YOU HAVE SELECT WRONG MODE PLEASE SELECT interactive OR file MODE OR exit to out of the project ") 
