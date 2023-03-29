import unittest
from .packages import Packages
from .packages import Package
from .input_validation import *


class TestDeliveryCostInput(unittest.TestCase):

    def test_add_package_input_validation(self):
        with self.assertRaises(TypeError):
            Package("PKG1", "string value", 5, "OFR001", 100)
        with self.assertRaises(TypeError):
            Package("PKG2", 10, "string value", "OFR001", 100)
        with self.assertRaises(TypeError):
            Package("PKG2", 10, 5, "OFR001", "string value")

    def test_negative_value(self):
        self.assertEqual(validate_float(-0.1231), "Invalid input. Value must be more than 0", "Not the same value for "
                                                                                              "negative float")
        self.assertEqual(validate_int(-1231), "Invalid input. Value must be more than 0", "Not the same value for "
                                                                                          "negative integer")

    def test_invalid_value_for_float(self):
        self.assertEqual(validate_float("not a float"), "Invalid input. Not a float.", "Not the same value for "
                                                                                       "invalid float")

    def test_invalid_value_for_int(self):
        self.assertEqual(validate_int("not an int"), "Invalid input. Not an integer.", "Not the same value for "
                                                                                       "invalid integer")

    def test_empty_string_input(self):
        self.assertEqual(validate_str(""), "Invalid input. Empty string given.", "Empty string not detected properly")
