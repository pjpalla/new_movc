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

        self.template_path = r"C:\Users\piepalla\PycharmProjects\new_movc\config\allegato7_base.xlsx"
        # self.province_dir = r"C:\Users\piepalla\PycharmProjects\new_movc\all7\movc\cagliari\MOVC_CA_GENNAIO_2016.xlsx"
        self.file_example = r"C:\Users\piepalla\PycharmProjects\new_movc\all7\movc\cagliari\MOVC_CA_GENNAIO_2016.xlsx"
        self.all7 = All7(2016, "città metropolitana di cagliari", self.template_path)
        self.all7.load_xl(self.file_example)



    def tearDown(self):
        pass


    def test_get_alberghi(self):
        tot_arrivi_residenti = self.all7.get_alberghi()
        self.logger.debug(tot_arrivi_residenti)

        tot_arrivi_non_residenti = self.all7.get_alberghi(category='non residenti')
        self.logger.debug(tot_arrivi_non_residenti)

        tot_presenze_residenti = self.all7.get_alberghi(type='presenze')
        self.logger.debug(tot_presenze_residenti)
        tot_presenze_non_residenti = self.all7.get_alberghi(type='presenze', category='non residenti')
        self.logger.debug(tot_presenze_non_residenti)


    # def test_get_presenze_residenti_alberghi(self):
    #     tot_presenze = self.all7.get_presenze_residenti_alberghi()
    #     self.logger.debug(tot_presenze)

    def test_get_alloggi(self):
        tot_arrivi_residenti = self.all7.get_alloggi()
        self.assertEqual(tot_arrivi_residenti, 1716)
        tot_arrivi_non_residenti = self.all7.get_alloggi(category='non residenti')

        tot_presenze_residenti = self.all7.get_alloggi(type='presenze')
        self.logger.debug(tot_presenze_residenti)
        tot_presenze_non_residenti = self.all7.get_alloggi(type='presenze', category='non residenti')
        self.logger.debug(tot_presenze_non_residenti)


    def test_get_campeggi(self):
        tot_arrivi_residenti = self.all7.get_campeggi()
        self.logger.debug(tot_arrivi_residenti)
        tot_arrivi_non_residenti = self.all7.get_campeggi(category='non residenti')
        self.logger.debug(tot_arrivi_non_residenti)

        tot_presenze_residenti = self.all7.get_campeggi(type='presenze')
        self.logger.debug(tot_presenze_residenti)
        tot_presenze_non_residenti = self.all7.get_campeggi(type='presenze', category='non residenti')
        self.logger.debug(tot_presenze_non_residenti)


    def test_get_altri_alloggi(self):
        tot_arrivi_residenti = self.all7.get_altri_alloggi()
        self.logger.debug(tot_arrivi_residenti)
        tot_arrivi_non_residenti = self.all7.get_altri_alloggi(category='non residenti')
        self.logger.debug(tot_arrivi_non_residenti)

        tot_presenze_residenti = self.all7.get_altri_alloggi(type="presenze")
        self.logger.debug(tot_presenze_residenti)
        tot_presenze_non_residenti = self.all7.get_altri_alloggi(type='presenze', category='non residenti')

