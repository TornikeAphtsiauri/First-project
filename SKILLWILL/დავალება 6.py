class Heart:
    def __init__(self, usage):
        self._usage = usage

    @property
    def state(self):
        if self._usage > 70:
            return "High blood pressure"
        else:
            return "Feeling good"


class Brain:
    def __init__(self, usage):
        self._usage = usage

    @property
    def state(self):
        if self._usage > 90:
            return "Tired"
        else:
            return "Rested"


class Leg:
    def __init__(self, moving_speed):
        self._moving_speed = moving_speed

    @property
    def movement(self):
        if self._moving_speed > 10:
            return "Running"
        elif 0 < self._moving_speed <= 10:
            return "Walking"
        else:
            return "Standing"


class Person:
    def __init__(self):
        heart_usage = int(input("Enter heart usage percentage: "))
        self.heart = Heart(heart_usage)

        brain_usage = int(input("Enter brain usage percentage: "))
        self.brain = Brain(brain_usage)

        leg_speed = float(input("Enter leg speed: "))
        self.leg = Leg(leg_speed)


# Example usage:
if __name__ == "__main__":
    person = Person()
    print("Heart state:", person.heart.state)
    print("Brain state:", person.brain.state)
    print("moving speed:", person.leg.movement)
