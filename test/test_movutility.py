__author__ = 'pg'

import unittest
import os
from movc.movutility import MovUtility


class TestMovUtilty(unittest.TestCase):

    def setUp(self):
        self.utility = MovUtility()
        #self.path = "C:\\Users\\piepalla\\PycharmProjects\\new-movc\\movs"

    def tearDown(self):
        self.utility = None


    def test_init(self):
        self.assertIsNotNone(self.utility)


    def test_default_io_config(self):
        input_dir =  self.utility.default_io_config()[0]
        output_dir = self.utility.default_io_config()[1]
        mapping_dir = self.utility.default_io_config()[2]
        self.assertEqual(r"C:\Users\piepalla\PycharmProjects\new_movc\data", input_dir)
        self.assertEqual(r"C:\Users\piepalla\PycharmProjects\new_movc\output", output_dir)
        self.assertEqual(r"C:\Users\piepalla\PycharmProjects\new_movc\config", mapping_dir)

    def test_merge_movs(self):
        #self.assertRaises(NotADirectoryError, MovUtility.merge_movs(""))

        self.utility.merge_movs(2016, 1)

    def test_get_merged_file(self):
       desired_file_path = "C:\\Users\piepalla\\PycharmProjects\\new_movc\\data\\2016\\01\\all_012016.txt"
       m = MovUtility()
       filepath = m.get_merged_file(2016, 1)
       self.assertEqual(desired_file_path, filepath)


    def test_get_movc(self):
        province_name = "cagliari"
        year = 2016
        month = 1
        self.assertEqual("pippo", self.utility.get_movc(province_name, year, month))


    def test_get_config_io_paths(self):
        year = 2016
        month = 1
        self.assertEqual("C:\\Users\\piepalla\\PycharmProjects\\new_movc\\data\\2016\\01", self.utility.config_io_paths(year, month))


    def test_get_all7_base_dir(self):
        mu = MovUtility()
        base_dir = mu.get_all7_base_dir()
        print(base_dir)