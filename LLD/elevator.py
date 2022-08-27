from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List
from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH


class ElevatorStates(Enum):
    IDLE = 0
    MOVING = 1
    STOP = 2


class Directions(Enum):
    UP = 0
    DOWN = 1


class IButton(metaclass=ABCMeta):
    @abstractmethod
    def process_request(self, src, dest, is_up):
        pass


class Floorbutton(IButton):
    def __init__(self, id, is_up) -> None:
        self.id = id
        self.is_up = is_up

    def process_request(self, src, dest, is_up):
        """Send request to DisPatcher"""


class Elevatorbutton(IButton):
    def __init__(self, id, dest, is_up) -> None:
        self.id = id
        self.is_up = is_up

    def process_request(self, src, dest, is_up):
        """Send request to DisPatcher"""


class Floor:
    def __init__(self, id, floor_buttons: List[Floorbutton]) -> None:
        self.id = id
        self.floor_buttons = floor_buttons


class Door:
    def __init__(self, is_open) -> None:
        self.is_open = is_open

    def door_opened(self):
        print("Door Opened")

    def door_closed(self):
        print("Door closed")


class Elevator:
    def __init__(
        self,
        id,
        max_weight,
        passenger_cnt,
        is_available,
        elevator_buttons: List[Elevatorbutton],
    ) -> None:
        self.id = id
        self.max_weight = max_weight
        self.passenger_cnt = passenger_cnt
        self.is_available = is_available
        self.elevator_buttons = elevator_buttons

    def move(self, src, dest):
        """Move the elevator"""


class Dispatcher:
    def __init__(self, floors, elevators) -> None:
        self.floors = floors
        self.elevators = elevators

    def send_request_to_elevator(id, src, dest, direction):
        """Send Request to Elevators"""


if __name__ == "__main__":

    fbup = Floorbutton(1, True)
    fbdown = Floorbutton(2, False)

    floor_btn_list = []
    floor_btn_list.append(fbup, fbdown)

    floor1 = Floor(1, floor_btn_list)
    floor2 = Floor(2, floor_btn_list)
    floor3 = Floor(3, floor_btn_list)
    floor4 = Floor(4, floor_btn_list)
    floor5 = Floor(5, floor_btn_list)
