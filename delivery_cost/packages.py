from .package import Package
from .input_validation import validate_int_input, validate_string_input, validate_float_input


class Packages:
    def __init__(self, base_cost, no_of_packages = 0):
        self.packages = []
        self.base_cost = base_cost
        self.no_of_packages = no_of_packages

    def add_package(self, package):
        self.packages.append(package)
        self.no_of_packages += 1

    def run_add_package(self):
        for i in range(self.no_of_packages):
            package_id = validate_string_input("Please enter the package ID: ")
            weight = validate_float_input("Please enter the package weight (in kg): ")
            distance = validate_float_input("Please enter the package distance (in km): ")
            offer_code = validate_string_input("Please enter the offer code (or NA for no discount): ")
            package = Package(package_id, weight, distance, offer_code, self.base_cost)
            self.packages.append(package)