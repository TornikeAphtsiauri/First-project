from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def start_engine(self):
        print("Car started")

    def stop_engine(self):
        print("Car stopped")


class SportCar(Car):
    def start_engine(self):
        super().start_engine()
        return f"Max speed: {self.max_speed}"

    def stop_engine(self):
        result = super().stop_engine()
        self.current_speed = 0
        return result


# Example usage:
car = SportCar(max_speed=200)
car.start_engine()  # Output: Car started. Max speed: 200
car.stop_engine()  # Output: Car stopped.
