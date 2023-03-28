#!/usr/bin/env python

class Package:
    def __init__(self, package_id, weight, distance, offer_code):
        self.package_id = package_id
        self.weight = weight
        self.distance = distance
        self.offer_code = offer_code


class Delivery:
    def __init__(self, base_cost):
        self.base_cost = base_cost
        self.packages = []
        self.delivery_time = 0

    def add_package(self, package):
        self.packages.append(package)

    def estimate_delivery_time(self, no_of_vehicles, max_speed, max_weight):
        total_weight = sum(package.weight for package in self.packages)
        total_distance = sum(package.distance for package in self.packages)
        time = (total_distance / max_speed) + (total_weight / max_weight)
        return time / no_of_vehicles

    def deliver_packages(self, no_of_vehicles, max_speed, max_weight):
        sorted_packages = sorted(self.packages, key=lambda x: x.weight, reverse=True)
        delivery_time = self.estimate_delivery_time(no_of_vehicles, max_speed, max_weight)
        for package in sorted_packages:
            if delivery_time > self.delivery_time:
                self.delivery_time = delivery_time
            if len(self.packages) == 0:
                break
            if package.weight <= max_weight:
                self.packages.remove(package)
        return delivery_time


class Vehicle:
    def __init__(self, max_weight, max_speed):
        self.max_weight = max_weight
        self.max_speed = max_speed
        self.current_weight = 0

    def can_carry(self, package):
        return self.current_weight + package.weight <= self.max_weight

    def add_package(self, package):
        self.current_weight += package.weight

    def deliver_packages(self, packages):
        total_weight = sum(package.weight for package in packages)
        total_distance = sum(package.distance for package in packages)
        delivery_time = total_distance / self.max_speed
        self.current_weight = 0
        return delivery_time


class DeliveryScheduler:
    def __init__(self, vehicles):
        self.deliveries = []
        self.vehicles = vehicles

    def add_delivery(self, delivery):
        self.deliveries.append(delivery)

    def schedule_deliveries(self):
        for delivery in self.deliveries:
            while len(delivery.packages) > 0:
                available_vehicles = [vehicle for vehicle in self.vehicles if vehicle.can_carry(delivery.packages[0])]
                if len(available_vehicles) > 0:
                    vehicle = available_vehicles[0]
                    packages_to_deliver = [package for package in delivery.packages if vehicle.can_carry(package)]
                    for package in packages_to_deliver:
                        delivery.packages.remove(package)
                        vehicle.add_package(package)
                    delivery_time = vehicle.deliver_packages(packages_to_deliver)
                    delivery.delivery_time += delivery_time
                else:
                    break
        self.deliveries = []


def main():
    # Define an array of vehicles
    vehicles = [
        Vehicle(100, 50),
        Vehicle(200, 70)
    ]

    # Create a new delivery scheduler with the array of vehicles
    scheduler = DeliveryScheduler(vehicles)

    # Create a new delivery object
    delivery1 = Delivery(10.0)

    # Add packages to the delivery
    package1 = Package("001", 50.0, 100.0, "NA")
    package2 = Package("002", 75.0, 150.0, "DISC10")
    package3 = Package("003", 100.0, 300.0, "NA")
    package4 = Package("004", 150.0, 250.0, "DISC20")

    delivery1.add_package(package1)
    delivery1.add_package(package2)
    delivery1.add_package(package3)
    delivery1.add_package(package4)

    # Add the delivery to the scheduler
    scheduler.add_delivery(delivery1)

    print(scheduler.deliveries[0].packages)
    # Schedule the deliveries
    scheduler.schedule_deliveries()

    print(scheduler.deliveries)
    # Print the delivery times for each delivery
    for delivery in scheduler.deliveries:
        print(f"Delivery time for {len(delivery.packages)} packages: {delivery.delivery_time:.2f} hours")


if __name__ == '__main__':
    main()
