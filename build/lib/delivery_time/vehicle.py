class Vehicle:

    def __init__(self, speed, max_weight):
        self.speed = speed
        self.max_weight = max_weight
        self.available_in = 0
        self.available = True
        self.hour_past = 0

    def update_status(self, status):
        self.available = status

    def add_delivery_time(self, time):
        self.available_in += time

        if self.available_in > 0 and self.available:
            self.hour_past += time
            self.update_status(False)

    def minus_delivery_time(self, time):
        self.available_in -= time

        if self.available_in <= 0 and not self.available:
            self.available_in = 0
            self.update_status(True)
