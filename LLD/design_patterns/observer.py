class Publisher:
    def __init__(self, name) -> None:
        self.name = name

    def update(self, message: str):
        print(f"Got message: {message} for {self.name}")


class Subsriber:
    def __init__(self) -> None:
        self.subscribers = set()

    def register(self, publisher):
        self.subscribers.add(publisher)

    def unregister(self, publisher):
        self.subscribers.discard(publisher)

    def notify(self, message):
        for pub in self.subscribers:
            pub.update(message)


if __name__ == "__main__":

    pub1 = Publisher("Ayan")
    pub2 = Publisher("Debamita")
    pub3 = Publisher("Debarati")

    sub = Subsriber()

    sub.register(pub1)
    sub.register(pub2)
    sub.register(pub3)

    sub.notify("Lunch Time")
    sub.unregister(pub1)
    sub.notify("Lets go for a trip")
