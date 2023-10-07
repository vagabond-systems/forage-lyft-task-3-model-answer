class Tire:
    def __init__(self, tire_type, tire_wear_array):
        self.tire_type = tire_type
        self.tire_wear_array = tire_wear_array

    def is_service_needed(self):
        pass  # This will be implemented in the subclasses


class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        super().__init__('Carrigan', tire_wear_array)

    def is_service_needed(self):
        # Check if any tire's wear is greater than or equal to 0.9
        return any(wear >= 0.9 for wear in self.tire_wear_array)


class OctoprimeTire(Tire):
    def __init__(self, tire_wear_array):
        super().__init__('Octoprime', tire_wear_array)

    def is_service_needed(self):
        # Check if the sum of all tire wears is greater than or equal to 3
        return sum(self.tire_wear_array) >= 3


