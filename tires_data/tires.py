from serviceable import Serviceable


class Tires(Serviceable):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        pass
