import sys
sys.path.insert(0, "..")

import unittest
from .delivery import Delivery
from delivery_cost.package import Package
from .vehicle import Vehicle


class TestDelivery(unittest.TestCase):

    def setUp(self):
        # create delivery object with two vehicles
        self.base_cost = 100
        max_speed = 70
        max_weight = 200
        self.delivery = Delivery(max_speed)
        vehicle1 = Vehicle(max_speed, max_weight)
        vehicle2 = Vehicle(max_speed, max_weight)
        self.delivery.add_vehicle(vehicle1)
        self.delivery.add_vehicle(vehicle2)

        # create packages to be delivered
        self.package1 = Package("PKG1", 50.0, 30, "OFR001", self.base_cost)
        self.package2 = Package("PKG2", 75.0, 125, "OFR008", self.base_cost)
        self.package3 = Package("PKG3", 175.0, 100, "OFR003", self.base_cost)
        self.package4 = Package("PKG4", 110.0, 60, "OFR002", self.base_cost)
        self.package5 = Package("PKG5", 155.0, 95, "NA", self.base_cost)
        self.delivery.add_package(self.package1)
        self.delivery.add_package(self.package2)
        self.delivery.add_package(self.package3)
        self.delivery.add_package(self.package4)
        self.delivery.add_package(self.package5)

        # estimate delivery time for every package
        self.delivery.estimate_delivery_time()

    def test_package_cost(self):
        # check that package cost is calculated correctly
        self.assertAlmostEqual(self.package1.total_cost, 750, delta=0.01)
        self.assertAlmostEqual(self.package2.total_cost, 1475, delta=0.01)
        self.assertAlmostEqual(self.package3.total_cost, 2350, delta=0.01)
        self.assertAlmostEqual(self.package4.total_cost, 1500, delta=0.01)
        self.assertAlmostEqual(self.package5.total_cost, 2125, delta=0.01)

    def test_package_cost_after_discount(self):
        # check that package cost after discount is calculated correctly
        self.assertAlmostEqual(self.package1.final_total_cost, 750, delta=0.01)
        self.assertAlmostEqual(self.package1.total_discount, 0, delta=0.01)
        self.assertAlmostEqual(self.package2.final_total_cost, 1475, delta=0.01)
        self.assertAlmostEqual(self.package2.total_discount, 0, delta=0.01)
        self.assertAlmostEqual(self.package3.final_total_cost, 2350, delta=0.01)
        self.assertAlmostEqual(self.package3.total_discount, 0, delta=0.01)
        self.assertAlmostEqual(self.package4.final_total_cost, 1395, delta=0.01)
        self.assertAlmostEqual(self.package4.total_discount, 105, delta=0.01)
        self.assertAlmostEqual(self.package5.final_total_cost, 2125, delta=0.01)
        self.assertAlmostEqual(self.package5.total_discount, 0, delta=0.01)

    def test_delivery_time(self):
        # check that delivery time is calculated correctly
        self.assertAlmostEqual(self.package1.estimate_delivery_time, 0.43, delta=0.02)
        self.assertAlmostEqual(self.package2.estimate_delivery_time, 1.79, delta=0.02)
        self.assertAlmostEqual(self.package3.estimate_delivery_time, 1.43, delta=0.02)
        self.assertAlmostEqual(self.package4.estimate_delivery_time, 0.86, delta=0.02)
        self.assertAlmostEqual(self.package5.estimate_delivery_time, 1.36, delta=0.02)

    def test_best_package_combination(self):
        # check that best package combination is selected correctly
        best_combination, longest_route, longest_id = self.delivery.best_package_combination(self.delivery.packages,
                                                                                             200)
        self.assertEqual(best_combination, ['PKG2', 'PKG4'])
        self.assertAlmostEqual(longest_route, 125.0, delta=0.01)
        self.assertEqual(longest_id, 'PKG2')

    def test_do_delivery(self):
        # check that packages are delivered and history is recorded correctly
        self.delivery.do_delivery()
        self.assertEqual(len(self.delivery.packages), 2)
        self.assertEqual(len(self.delivery.history_packages), 3)
        self.assertEqual(self.package1.final_delivery_time, 0.42)
        self.assertEqual(self.package3.final_delivery_time, 1.42)

    def test_estimate_delivery_time_with_waiting(self):
        # check that final delivery time with waiting is calculated correctly
        while True:
            self.delivery.do_delivery()

            if len(self.delivery.packages) == 0:
                break

        self.assertAlmostEqual(self.package1.final_delivery_time, 3.98, delta=0.02)
        self.assertAlmostEqual(self.package2.final_delivery_time, 1.78, delta=0.02)
        self.assertAlmostEqual(self.package3.final_delivery_time, 1.42, delta=0.02)
        self.assertAlmostEqual(self.package4.final_delivery_time, 0.85, delta=0.02)
        self.assertAlmostEqual(self.package5.final_delivery_time, 4.18, delta=0.02)

    def test_estimate_delivery_time_with_waiting_2(self):
        # check that final delivery time with waiting is calculated correctly

        self.package6 = Package("PKG6", 50.0, 100, "OFR002", self.base_cost)
        self.package7 = Package("PKG7", 50.0, 100, "OFR001", self.base_cost)
        self.package8 = Package("PKG8", 150.0, 100, "OFR003", self.base_cost)
        self.package9 = Package("PKG9", 99.0, 100, "OFR001", self.base_cost)
        self.package10 = Package("PKG10", 100.0, 100, "OFR001", self.base_cost)
        self.delivery.add_package(self.package6)
        self.delivery.add_package(self.package7)
        self.delivery.add_package(self.package8)
        self.delivery.add_package(self.package9)
        self.delivery.add_package(self.package10)

        self.delivery.estimate_delivery_time()

        while True:
            self.delivery.do_delivery()

            if len(self.delivery.packages) == 0:
                break

        self.assertAlmostEqual(self.package1.final_delivery_time, 0.42, delta=0.02)
        self.assertAlmostEqual(self.package2.final_delivery_time, 5.34, delta=0.02)
        self.assertAlmostEqual(self.package3.final_delivery_time, 4.98, delta=0.02)
        self.assertAlmostEqual(self.package4.final_delivery_time, 4.41, delta=0.02)
        self.assertAlmostEqual(self.package5.final_delivery_time, 7.75, delta=0.02)
        self.assertAlmostEqual(self.package6.final_delivery_time, 1.42, delta=0.02)
        self.assertAlmostEqual(self.package7.final_delivery_time, 1.42, delta=0.02)
        self.assertAlmostEqual(self.package8.final_delivery_time, 1.42, delta=0.02)
        self.assertAlmostEqual(self.package9.final_delivery_time, 8.54, delta=0.02)
        self.assertAlmostEqual(self.package10.final_delivery_time, 1.42, delta=0.02)

    def test_estimate_delivery_time_with_waiting_3(self):
        # check that final delivery time with waiting is calculated correctly

        added = False

        self.package6 = Package("PKG6", 50.0, 100, "OFR002", self.base_cost)
        self.package7 = Package("PKG7", 50.0, 100, "OFR001", self.base_cost)
        self.package8 = Package("PKG8", 150.0, 100, "OFR003", self.base_cost)
        self.package9 = Package("PKG9", 99.0, 100, "OFR001", self.base_cost)
        self.package10 = Package("PKG10", 100.0, 100, "OFR001", self.base_cost)

        while True:
            self.delivery.do_delivery()

            if len(self.delivery.packages) <= 3 and not added:
                self.delivery.add_package(self.package6)
                self.delivery.add_package(self.package7)
                self.delivery.add_package(self.package8)
                self.delivery.add_package(self.package9)
                self.delivery.add_package(self.package10)

                self.delivery.estimate_delivery_time()

                added = True

            if len(self.delivery.packages) == 0:
                break

        self.assertAlmostEqual(self.package1.final_delivery_time, 3.26, delta=0.02)
        self.assertAlmostEqual(self.package2.final_delivery_time, 1.78, delta=0.02)
        self.assertAlmostEqual(self.package3.final_delivery_time, 1.42, delta=0.02)
        self.assertAlmostEqual(self.package4.final_delivery_time, 0.85, delta=0.02)
        self.assertAlmostEqual(self.package5.final_delivery_time, 7.02, delta=0.02)
        self.assertAlmostEqual(self.package6.final_delivery_time, 4.26, delta=0.02)
        self.assertAlmostEqual(self.package7.final_delivery_time, 4.98, delta=0.02)
        self.assertAlmostEqual(self.package8.final_delivery_time, 4.98, delta=0.02)
        self.assertAlmostEqual(self.package9.final_delivery_time, 7.82, delta=0.02)
        self.assertAlmostEqual(self.package10.final_delivery_time, 4.26, delta=0.02)

    def test_add_new_package_with_invalid_data(self):
        # add package with invalid data

        with self.assertRaises(TypeError):
            self.package6 = Package("PKG6", "not a number", 100, "OFR002", self.base_cost)
            self.delivery.add_package(self.package6)

        with self.assertRaises(TypeError):
            self.package6 = Package("PKG6", 100, "not a number", "OFR002", self.base_cost)
            self.delivery.add_package(self.package6)

        with self.assertRaises(TypeError):
            self.package6 = Package("PKG6", 100, 100, "OFR002", "not a number")
            self.delivery.add_package(self.package6)

    def test_create_delivery_object_with_invalid_data(self):
        # create delivery object with invalid data

        base_cost = 100
        max_speed = 70
        max_weight = 200
        wrong_value = "not a number"

        with self.assertRaises(TypeError):
            delivery = Delivery(wrong_value)
            vehicle1 = Vehicle(max_speed, max_weight)
            delivery.add_vehicle(vehicle1)
            package6 = Package("PKG6", 100, 100, "OFR002", base_cost)
            delivery.add_package(package6)
            delivery.estimate_delivery_time()
            delivery.do_delivery()

    def test_create_delivery_object_with_invalid_vehicle_data(self):
        # create delivery object with invalid data

        base_cost = 100
        max_speed = 70
        max_weight = 200
        wrong_value = "not a number"

        with self.assertRaises(TypeError):
            delivery = Delivery(max_speed)
            vehicle1 = Vehicle(wrong_value, max_weight)
            delivery.add_vehicle(vehicle1)
            package6 = Package("PKG6", 100, 100, "OFR002", base_cost)
            delivery.add_package(package6)
            delivery.estimate_delivery_time()
            delivery.do_delivery()
        with self.assertRaises(TypeError):
            delivery = Delivery(max_speed)
            vehicle1 = Vehicle(max_speed, wrong_value)
            delivery.add_vehicle(vehicle1)
            package6 = Package("PKG6", 100, 100, "OFR002", base_cost)
            delivery.add_package(package6)
            delivery.estimate_delivery_time()
            delivery.do_delivery()
