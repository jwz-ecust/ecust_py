class Bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$800"

a = Bank()
while True:
    print a.create_atm().next()