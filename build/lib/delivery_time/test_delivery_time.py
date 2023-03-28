import unittest
from .delivery import Delivery
from .package import Package
from .vehicle import Vehicle


class TestDelivery(unittest.TestCase):

    def setUp(self):
        # create delivery object with two vehicles
        base_cost = 100
        max_speed = 70
        max_weight = 200
        self.delivery = Delivery(base_cost, max_speed, max_weight)
        vehicle1 = Vehicle(max_speed, max_weight)
        vehicle2 = Vehicle(max_speed, max_weight)
        self.delivery.add_vehicle(vehicle1)
        self.delivery.add_vehicle(vehicle2)

        # create packages to be delivered
        self.package1 = Package("PKG1", 50.0, 30, "OFR001", base_cost)
        self.package2 = Package("PKG2", 75.0, 125, "OFR008", base_cost)
        self.package3 = Package("PKG3", 175.0, 100, "OFR003", base_cost)
        self.package4 = Package("PKG4", 110.0, 60, "OFR002", base_cost)
        self.package5 = Package("PKG5", 155.0, 95, "NA", base_cost)
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