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
        # self.file_example = r"C:\Users\piepalla\PycharmProjects\new_movc\all7\movc\cagliari\MOVC_CA_GENNAIO_2016.xlsx"
        self.file_example = r"C:\Users\piepalla\PycharmProjects\new_movc\all7\movc\2016\cagliari\MOVC_CA_Gennaio_2016.xlsx"
        self.all7 = All7(self.template_path, 2016, "PROVINCIA DI SASSARI")
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
        # self.assertEqual(tot_arrivi_residenti, 1716)
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


    def test_get_giornate_letto(self):
        tot_giornate_letto = self.all7.get_giornate_letto()
        #self.assertEqual(tot_giornate_letto, 78937)
        self.logger.debug(tot_giornate_letto)


    def test_get_giornate_camere(self):
        tot_giornate_camere_disponibili = self.all7.get_giornate_camere()
        # self.assertEqual(tot_giornate_camere_disponibili, 40213)
        self.logger.debug("totale giornate camere disponibili %s"%tot_giornate_camere_disponibili)
        tot_giornate_camere_occupate = self.all7.get_giornate_camere(type = 'occupate')
        self.logger.debug("totale giornate camere occupate %s" % tot_giornate_camere_occupate)
        # self.assertEqual(tot_giornate_camere_occupate, 14606)


    def test_load_xl(self):
        pass


    def test_check_province(self):
        province = self.all7.check_province(self.all7.movc)
        self.assertEqual('PROVINCIA DI CAGLIARI', province)


    def test_check_year(self):
        year = self.all7.check_year(self.all7.movc)
        self.assertEqual('2016', year)

    def test_build_xl(self):
        import time
        movc_dir = r"C:\Users\piepalla\PycharmProjects\new_movc\all7\movc\2016\cagliari"
        output_file = os.path.join(movc_dir, "pippo.xlsx")
        start_time = time.time()
        self.all7.build_xl(movc_dir, output_file)
        elapsed_time = time.time() - start_time
        self.logger.info("elapsed time: %s"%elapsed_time)
