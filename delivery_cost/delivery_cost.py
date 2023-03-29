#!/usr/bin/env python
from .packages import Packages
from .package import Package
from .input_validation import validate_int_input


def print_packages(packages):
    from prettytable import PrettyTable
    table = PrettyTable()

    table.field_names = ["Package ID", "Discount", "Total Cost"]

    for package in packages:
        table.add_row([package.package_id, package.total_discount, package.final_total_cost])

    print(table)


def main():
    input_type = input("Please select input type: (auto/manual) ")

    if input_type == 'auto':
        base_cost = 100
        package1 = Package("PKG1", 5, 5, "OFR001", base_cost)
        package2 = Package("PKG1", 15, 5, "OFR002", base_cost)
        package3 = Package("PKG1", 10, 100, "OFR003", base_cost)
        package4 = Package("PKG1", 231, 15, "OFR003", base_cost)
        packages = Packages(base_cost)
        packages.add_package(package1)
        packages.add_package(package2)
        packages.add_package(package3)
        packages.add_package(package4)
    else:
        base_cost = validate_int_input("Please enter the base delivery cost: ")
        no_of_packages = validate_int_input("Please enter the number of packages: ")
        packages = Packages(base_cost, no_of_packages)
        packages.run_add_package()

    print_packages(packages.packages)


if __name__ == '__main__':
    main()
