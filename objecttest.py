from re import X


class Pet:
    x = 0

    def __init__(self) -> None:
        print('Constructed')

    def party(self):
        self.x = self.x + 1
        print('x equals to ', self.x)

    def __del__(self):
        print('Destructed')

petv = Pet()
petv.party()
petv.party()
