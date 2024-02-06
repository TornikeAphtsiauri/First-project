class Car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car

    # Getter methods to access private attributes
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_production_year(self):
        return self.__production_year

    def get_color(self):
        return self.__color

    def get_horse_power(self):
        return self.__horse_power

    def is_sport_car(self):
        return self.__is_sport_car

    # Setter method to modify the value of is_sport_car
    def set_sport_car(self, is_sport_car):
        self.__is_sport_car = is_sport_car

    # Method to change the color
    def change_color(self, new_color):
        if isinstance(new_color, str):
            if new_color.lower() == self.__color.lower():
                return False  # Color remains the same
            else:
                self.__color = new_color
                return True  # Color changed successfully
        else:
            raise ValueError("Color must be a string value")

    # Method to increase horse power
    def increase_horse_power(self, hp):
        if isinstance(hp, int) and hp > 0:
            self.__horse_power += hp
            return True  # Horse power increased successfully
        else:
            return False  # Horse power remains the same or invalid input


# Example usage of the Car class
car1 = Car("Toyota", "Prius C", 2012, "Gray", 175)
print(car1.increase_horse_power(50))  # Output: True (horse power increased successfully)
print(car1.get_horse_power())         # Output: 250

print(car1.increase_horse_power(-10))  # Output: False (horse power remains the same or invalid input)
print(car1.get_horse_power())         # Output: 250
