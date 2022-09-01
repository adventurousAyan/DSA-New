from abc import ABC, abstractmethod


class Elevator:

    _state = None

    def __init__(self, state) -> None:

        self.set_state(state)

    def set_state(self, state):
        self._state = state
        self._state.elevator = self

    def presentState(self):
        print(f"Elevator is in {type(self._state).__name__}")

    def push_up_button(self):
        self._state.push_up_button()

    def push_down_button(self):
        self._state.push_down_button()

    def push_up_down_button(self):
        print("Both buttons cannot be pressed at same time")

    def push_no_button(self):
        print("Please press a button")


class State(ABC):
    @property
    def elevator(self):
        return self._elevator

    @elevator.setter
    def elevator(self, elevator: Elevator):
        self._elevator = elevator

    @abstractmethod
    def push_up_button(self):
        pass

    @abstractmethod
    def push_down_button(self):
        pass


class FirstFloor(State):
    def push_up_button(self):
        print("Going to 2nd floor")
        self.elevator.set_state(SecondFloor())

    def push_down_button(self):
        print("Already at ground floor")


class SecondFloor(State):
    def push_up_button(self):
        print("Already on 2nd floor")

    def push_down_button(self):
        print("Going to 1st floor")
        self.elevator.set_state(FirstFloor())


if __name__ == "__main__":

    elevator = Elevator(FirstFloor())

    elevator.presentState()

    elevator.push_up_button()

    elevator.presentState()

    elevator.push_down_button()

    elevator.presentState()
