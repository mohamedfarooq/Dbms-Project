class raakin:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def user(self):
        print(f"Hello mr {self.name}, welcome to RAK BANK")
        sle = int(input("press 1 to get details: "))
        if sle == 1:
            print(f"DETAILS\nNAME={self.name}\nAGE={self.age}\nGENDER={self.gender}")
        elif sle != 1:
            print("wrong command.... try agin later")
            exit()


r = raakin("RAAKIN", 20, "MALE")
r.user()
print(r)