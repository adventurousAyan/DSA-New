from abc import ABCMeta, abstractmethod, abstractstaticmethod


class IHandler(metaclass=ABCMeta):
    @abstractstaticmethod
    def set_successor(successor):
        """"""

    @abstractstaticmethod
    def handle(amount):
        """"""


class Dispenser50(IHandler):
    def __init__(self) -> None:
        self.__successor = None

    def set_successor(self, successor):
        self.__successor = successor

    def handle(self, amount):
        if amount > 50:
            num = amount // 50
            rem = amount % 50

            print(f"Dispensing {num} 50 notes ")
            if rem != 0:
                self.__successor.handle(rem)
        else:
            self.__successor.handle(amount)


class Dispenser20(IHandler):
    def __init__(self) -> None:
        self.__successor = None

    def set_successor(self, successor):
        self.__successor = successor

    def handle(self, amount):
        if amount > 20:
            num = amount // 20
            rem = amount % 20

            print(f"Dispensing {num} 20 notes ")
            if rem != 0:
                self.__successor.handle(rem)
        else:
            self.__successor.handle(amount)


class Dispenser10(IHandler):
    def __init__(self) -> None:
        self.__successor = None

    def set_successor(self, successor):
        self.__successor = successor

    def handle(self, amount):
        if amount >= 10:
            num = amount // 10
            rem = amount % 10

            print(f"Dispensing {num} 10 notes ")
            if rem != 0:
                self.__successor.handle(rem)
        else:
            self.__successor.handle(amount)


class ATMDispenserChain:
    def __init__(self) -> None:
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()

        self.chain1.set_successor(self.chain2)
        self.chain2.set_successor(self.chain3)


if __name__ == "__main__":

    atm = ATMDispenserChain()

    amount = int(input("Please enter amount: "))

    if amount < 10 or amount % 10 != 0:
        print("Amount should be multiples of 10")
    else:
        atm.chain1.handle(amount)
