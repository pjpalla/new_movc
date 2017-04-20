__author__ = 'pg'
import unittest, logging
from all7.all7 import *
import os

class TestAll7(unittest.TestCase):
    def setUp(self):
        ### Set Logger ###
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        # console handler with level debug
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        self.template_path = r"config/allegato7_base.xlsx"
        # self.province_dir = r"C:\Users\piepalla\PycharmProjects\new_movc\all7\movc\cagliari\MOVC_CA_GENNAIO_2016.xlsx"
        self.file_example = r"MOVC_CA_GENNAIO_2016.xlsx"
        self.all7 = All7(2016, "città metropolitana di cagliari", self.template_path)
        self.all7.load_xl(self.file_example)



    def tearDown(self):
        pass


    def test_get_arrivi_residenti_alberghi(self):
        tot_arrivi = self.all7.get_arrivi_residenti_alberghi()
        self.logger.debug(tot_arrivi)


    def test_get_presenze_residenti_alberghi(self):
        tot_presenze = self.all7.get_presenze_residenti_alberghi()
        self.logger.debug(tot_presenze)

    def test_get_arrivi_alloggi(self):
        tot_arrivi = self.all7.get_arrivi_alloggi()
        self.assertEqual(tot_arrivi, 1492)