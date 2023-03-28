#!/usr/bin/env python

# use sys to reuse Package class
import sys
sys.path.insert(0,"..")

import math
from prettytable import PrettyTable
from delivery_cost.package import Package
from .delivery import Delivery
from .vehicle import Vehicle


def print_packages(packages):
    table = PrettyTable()

    table.field_names = [
        "Package ID",
        "Discount",
        "Total Cost",
        "Weight",
        "Distance",
        "Estimate Delivery Time",
        "Final Est Delivery Time"
    ]

    for package in packages:
        table.add_row([
            package.package_id,
            package.total_discount,
            package.final_total_cost,
            package.weight,
            package.distance,
            package.estimate_delivery_time,
            math.floor(package.final_delivery_time * 100) / 100
        ])

    print(table)


def main():
    input_type = input("Please select input type: (auto/manual) ")

    if input_type == 'auto':
        base_cost = 100
        max_speed = 70
        max_weight = 200
        delivery = Delivery(base_cost, max_speed, max_weight)
        vehicle1 = Vehicle(max_speed, max_weight)
        vehicle2 = Vehicle(max_speed, max_weight)
        delivery.add_vehicle(vehicle1)
        delivery.add_vehicle(vehicle2)
        package1 = Package("PKG1", 50.0, 30, "OFR001", base_cost)
        package2 = Package("PKG2", 75.0, 125, "OFR008", base_cost)
        package3 = Package("PKG3", 175.0, 100, "OFR003", base_cost)
        package4 = Package("PKG4", 110.0, 60, "OFR002", base_cost)
        package5 = Package("PKG5", 155.0, 95, "NA", base_cost)
        delivery.add_package(package1)
        delivery.add_package(package2)
        delivery.add_package(package3)
        delivery.add_package(package4)
        delivery.add_package(package5)
    else:
        base_cost = float(input("Please enter the base delivery cost: "))
        no_of_packages = int(input("Please enter the number of packages: "))
        no_of_vehicles = int(input("Please enter the number of vehicles available: "))
        max_speed = float(input("Please enter the maximum speed for all the vehicles (in km/h): "))
        max_weight = float(input("Please enter the maximum weight all the vehicles can carry (in kg): "))
        delivery = Delivery(base_cost, max_speed, max_weight)

        for _ in range(no_of_vehicles):
            vehicle = Vehicle(max_speed, max_weight)
            delivery.add_vehicle(vehicle)

        for i in range(no_of_packages):
            print(f"# {i+1}")
            package_id = input("Please enter the package ID: ")
            weight = float(input("Please enter the package weight (in kg): "))
            distance = float(input("Please enter the package distance (in km): "))
            offer_code = input("Please enter the offer code (or NA for no discount): ")
            package = Package(package_id, weight, distance, offer_code, base_cost)
            delivery.add_package(package)

    # estimate delivery time for every packages
    delivery.estimate_delivery_time()

    while True:
        delivery.do_delivery()

        if len(delivery.packages) == 0:
            break

    print_packages(delivery.history_packages)


if __name__ == '__main__':
    main()
