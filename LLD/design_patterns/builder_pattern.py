from abc import ABCMeta, abstractmethod, abstractstaticmethod


class House:
    def __init__(
        self, building_type="Apartment", no_of_doors=1, no_of_windows=2
    ) -> None:
        self.building_type = building_type
        self.no_of_doors = no_of_doors
        self.no_of_windows = no_of_windows

    def __str__(self) -> str:
        return f"This is a house {self.building_type} and {self.no_of_doors} doors and {self.no_of_windows} windows"


class IHouseBuilder(metaclass=ABCMeta):
    @abstractstaticmethod
    def set_building_type(self, value):
        """"""

    @abstractstaticmethod
    def set_no_of_doors(self, value):
        """"""

    @abstractstaticmethod
    def set_no_of_windows(self, value):
        """"""

    @abstractstaticmethod
    def get_results(self):
        """"""


class HouseBuilder(IHouseBuilder):
    def __init__(self):
        self.house = House()

    def set_building_type(self, value):
        self.house.building_type = value
        return self

    def set_no_of_doors(self, value):
        self.house.no_of_doors = value
        return self

    def set_no_of_windows(self, value):
        self.house.no_of_windows = value
        return self

    def get_results(self):
        return self.house


class Director:
    @staticmethod
    def construct():
        return (
            HouseBuilder()
            .set_building_type("Igloo")
            .set_no_of_doors(1)
            .set_no_of_windows(2)
            .get_results()
        )


if __name__ == "__main__":
    igloo = Director.construct()
    print(igloo)
