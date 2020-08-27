#Demonstrating Inheritence in Python


class One:
    def __init__(self):
        print("ONE!!!")

class Two(One):
    def __init__(self):
        super().__init__()
        print("TWO!!!")


Two()