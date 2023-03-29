import math
from itertools import combinations


class Delivery:
    def __init__(self, speed):
        self.speed = speed
        self.packages = []
        self.history_packages = []
        self.vehicles = []
        self.current_hour = 0

    def add_package(self, package):
        self.packages.append(package)

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def estimate_delivery_time(self):
        for package in self.packages:
            package.estimate_delivery_time = math.floor((package.distance / self.speed) * 100) / 100
            package.final_delivery_time = package.estimate_delivery_time

    def vehicle_available(self):
        available = False
        for vehicle in self.vehicles:
            if vehicle.available:
                available = True

        return available

    def run_time(self):
        self.current_hour += 0.01
        for vehicle in self.vehicles:
            if not vehicle.available:
                vehicle.minus_delivery_time(0.01)

    def do_delivery(self):
        if self.vehicle_available():
            for vehicle in self.vehicles:
                if not vehicle.available:
                    continue

                next_delivery_packages, longest_route, longest_id = self.best_package_combination(self.packages, vehicle.max_weight)
                delivery_time = math.floor((longest_route / vehicle.speed) * 100) / 100
                vehicle_current_hour = vehicle.hour_past
                vehicle.add_delivery_time(math.floor((delivery_time * 2) * 100) / 100)
                self.remove_packages_in_delivery(next_delivery_packages, vehicle_current_hour, longest_id, delivery_time)
                vehicle_current_hour += delivery_time

        self.run_time()

    def best_package_combination(self, package_list, max_weight):
        best_combination = []
        best_total_weight = 0
        longest_route = 0
        longest_id = None
        highest_no_of_packages = 0

        for i in range(1, len(package_list) + 1):
            for combination in combinations(package_list, i):
                total_weight = 0
                no_of_packages = len(combination)

                for package in combination:
                    total_weight += package.weight
                    if package.distance > longest_route:
                        longest_route = package.distance
                        longest_id = package.package_id

                if max_weight >= total_weight > best_total_weight or (
                        max_weight >= total_weight and no_of_packages > highest_no_of_packages):
                    best_combination = list([package.package_id for package in combination])
                    best_total_weight = total_weight
                    highest_no_of_packages = no_of_packages

        return [best_combination, longest_route, longest_id]

    def remove_packages_in_delivery(self, to_remove_packages, vehicle_current_hour, longest_id, delivery_time):
        available_packages = self.packages.copy()
        for package in available_packages:
            if package.package_id in to_remove_packages:
                if package.package_id == longest_id:
                    package.final_delivery_time = vehicle_current_hour + delivery_time
                else:
                    package.final_delivery_time += vehicle_current_hour
                self.history_packages.append(package)
                self.packages.remove(package)