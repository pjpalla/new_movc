__author__ = 'pg'
import unittest, logging
import os
from movc.new_movc import Movc
from movc.movc_parser import MovcParser
from movc.movxl import MovXL


class TestMovXL(unittest.TestCase):
    def setUp(self):
        ### Set Logger ###
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        #console handler with level debug
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        ############################

        ### Movc object creation
        map_path = r"C:\\Users\\piepalla\\PycharmProjects\\new_movc\\config\\mapping.csv"
        template_path = r"C:\\Users\\piepalla\\PycharmProjects\\new_movc\\config\\movc_base_2012.xlsx"
        movc_path = r"C:\Users\piepalla\PycharmProjects\new_movc\output\2016\01\movc_ca_012016.txt"
        input_dir = r"C:\Users\piepalla\PycharmProjects\new_movc\data"
        output_dir = r"C:\Users\piepalla\PycharmProjects\new_movc\output"


        self.movxl = MovXL(template_path, map_path, movc_path)
        # self.movc = Movc(1, 2016)
        # self.movc.set_mapper(self.map_path)
        # self.movc.set_input_dir(self.input_dir)
        # self.movc.set_output_dir(self.output_dir)


    def tearDown(self):
        self.movxl = None

    def test_init(self):
        self.assertIsNotNone(self.movxl)
        self.assertIsInstance(self.movxl, MovXL)


    def test_builXL(self):
        output_filename = r"C:\Users\piepalla\PycharmProjects\new_movc\output\2016\01\xltest1.xlsx"
        self.movxl.build_xl(output_filename)

    def test_add_summary(self):
        filepath = r"C:\Users\piepalla\Desktop\new_movc_012017\gennaio\MOVC_CA_GE_2017.xlsx"
        # output = r"C:\Users\piepalla\Desktop\new_movc_012017\gennaio\riepilogo.xlsx"
        self.movxl.add_summary(filepath)

