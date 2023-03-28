import unittest
from .packages import Packages
from .packages import Package


class TestDelivery(unittest.TestCase):

    def setUp(self):
        base_cost = 100
        self.package1 = Package("PKG1", 5, 5, "OFR001", base_cost)
        self.package2 = Package("PKG1", 15, 5, "OFR002", base_cost)
        self.package3 = Package("PKG1", 10, 100, "OFR003", base_cost)
        self.package4 = Package("PKG1", 231, 15, "OFR003", base_cost)
        self.packages = Packages(base_cost)
        self.packages.add_package(self.package1)
        self.packages.add_package(self.package2)
        self.packages.add_package(self.package3)
        self.packages.add_package(self.package4)

    def test_package_cost(self):
        # check that package cost is calculated correctly
        self.assertAlmostEqual(self.package1.total_cost, 175, delta=0.01)
        self.assertAlmostEqual(self.package2.total_cost, 275, delta=0.01)
        self.assertAlmostEqual(self.package3.total_cost, 700, delta=0.01)
        self.assertAlmostEqual(self.package4.total_cost, 2485, delta=0.01)

    def test_package_cost_after_discount(self):
        # check that package cost after discount is calculated correctly
        self.assertAlmostEqual(self.package1.final_total_cost, 175, delta=0.01)
        self.assertAlmostEqual(self.package1.total_discount, 0, delta=0.01)
        self.assertAlmostEqual(self.package2.final_total_cost, 275, delta=0.01)
        self.assertAlmostEqual(self.package2.total_discount, 0, delta=0.01)
        self.assertAlmostEqual(self.package3.final_total_cost, 665, delta=0.01)
        self.assertAlmostEqual(self.package3.total_discount, 35, delta=0.01)
        self.assertAlmostEqual(self.package4.final_total_cost, 2485, delta=0.01)
        self.assertAlmostEqual(self.package4.total_discount, 0, delta=0.01)