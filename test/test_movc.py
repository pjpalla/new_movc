__author__ = 'pg'
import unittest
import os, logging, sys
from movc.new_movc import Movc
from movc.consts import MAPPING_FILE
from movc.movutility import MovUtility

import pandas



# logger = logging.getLogger()

# stream_handler = logging.StreamHandler(sys.stdout)
# logger.addHandler(stream_handler)


class TestMovc(unittest.TestCase):
    def setUp(self):

        self.movc = Movc(1, 2016)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        #console handler with level debug
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        # self.logger.setLevel(10)
        self.map_path = r"C:\\Users\\piepalla\\PycharmProjects\\new_movc\\config\\mapping.csv"
        self.input_dir = r"C:\Users\piepalla\PycharmProjects\new_movc\data"
        self.output_dir = r"C:\Users\piepalla\PycharmProjects\new_movc\output"


    def tearDown(self):
        self.movc = None


    def test_init(self):
        movc = Movc(7, 2015)
        self.assertTrue(self, movc)


    def test_get_month(self):
        self.assertAlmostEqual(8, self.movc.get_month())
        self.logger.debug("****** logger")
        # stream_handler.stream = sys.stdout
        # print("AA")
        # logging.getLogger().info("BB")

    def test_get_year(self):
        self.assertAlmostEqual(2016, self.movc.get_year())


    def test_get_input_dir(self):
        self.movc.set_input_dir(self.input_dir)
        self.assertEqual("C:\\Users\\piepalla\\PycharmProjects\\new_movc\\data", self.movc.get_input_dir())
        self.assertEqual(r"C:\Users\piepalla\PycharmProjects\new_movc\data", self.movc.get_input_dir())


    def test_get_output_dir(self):
        self.movc.set_output_dir(self.output_dir)
        self.assertEqual(r"C:\Users\piepalla\PycharmProjects\new_movc\output", self.movc.get_output_dir())

    def test_get_mapper(self):

        self.movc.set_mapper(self.map_path)
        mapper = self.movc.get_mapper()
        self.assertIsNotNone(mapper)
        self.assertEqual(378, mapper.shape[0])
        self.assertEqual(5, mapper.shape[1])
        self.assertIsInstance(mapper, pandas.core.frame.DataFrame)
        self.assertEqual("com_new", list(mapper)[1])
        self.logger.debug(list(mapper))
        #self.logger.debug(mapper.ix[:, "prov_new"])
        # logging.debug(mapper.ix[:, "prov_new"])
        # self.logger.warning(mapper.ix[:, "prov_new"])

    def test_create_movc(self):

        movc = self.movc
        self.logger.debug(os.getcwd())
        movc.set_mapper(self.map_path)
        movc.set_input_dir(self.input_dir)
        movc.set_output_dir(self.output_dir)
        path = "C:\\Users\\piepalla\\PycharmProjects\\new_movc\\config\\movc.txt"
        try:
            self.assertRaises(FileNotFoundError, movc.create_movc("oristano", "lillo", "" ))
        except FileNotFoundError:
            print("Exception correctly raised!")

        movc.create_movc("cagliari", "")




    def test_create_movc2(self):
        movc = Movc(1, 2016)
        movc.set_mapper(self.map_path)
        movc.set_input_dir(self.input_dir)
        movc.set_output_dir(self.output_dir)
        movc.create_movc("nuoro")


    def test_validate(self):
        mapper_path = "C:\\Users\\piepalla\\PycharmProjects\\new_movc\\config\\mapping.csv"
        movc_path = "C:\\Users\\piepalla\\PycharmProjects\\new_movc\\output\\movc_nu_82016.txt"

        movc = Movc(month=8, year=2016)
        movc.set_mapper(mapper_path)
        movc.validate(movc_path)

    def test_validate2(self):
        movc = Movc(1, 2016)
        movc.set_mapper(self.map_path)
        movc.set_input_dir(self.input_dir)
        movc.set_output_dir(self.output_dir)

        file_to_validate = r"C:\Users\piepalla\PycharmProjects\new_movc\output\2016\01\movc_nu_012016.txt"
        movc.validate(file_to_validate)


    def test_get_province_name(self):
        movc = self.movc
        province_name = self.movc.get_province_name(292)
        self.assertEqual("città metropolitana di cagliari", province_name)
        province_name = self.movc.get_province_name(91)
        self.assertEqual('nuoro', province_name)
        province_name = self.movc.get_province_name(111)
        self.assertEqual('sud sardegna', province_name)
        province_name = self.movc.get_province_name(95)
        self.assertEqual('oristano', province_name)
        province_name = self.movc.get_province_name(90)
        self.assertEqual('sassari', province_name)
        # self.assertEqual('292', movc.create_movc("città metropolitana", ""))
        # self.assertEqual('90', movc.create_movc("sassari", ""))
        # self.assertEqual('111', movc.create_movc("sud sardegna", ""))
        # self.assertEqual('91', movc.create_movc("nuoro", ""))
        # self.assertEqual('95', movc.create_movc("oristano", ""))


    def test_get_movc(self):
        self.movc = Movc(1, 2016)
        self.movc.set_input_dir(self.input_dir)
        self.movc.set_output_dir(self.output_dir)
        movc_file = self.movc.get_movc("cagliari")
        self.logger.debug(movc_file)
        self.assertEqual(movc_file, r"C:\Users\piepalla\PycharmProjects\new_movc\output\2016\01\movc_ca_012016.txt")
        movc_file = self.movc.get_movc("sassari")
        self.assertEqual(movc_file, r"C:\Users\piepalla\PycharmProjects\new_movc\output\2016\01\movc_ss_012016.txt")
        self.logger.debug(movc_file)
        movc_file = self.movc.get_movc("sud sardegna")
        self.assertEqual(movc_file, r"C:\Users\piepalla\PycharmProjects\new_movc\output\2016\01\movc_sd_012016.txt")
        movc_file = self.movc.get_movc("pippo")
        self.logger.debug(movc_file)


    def test___missing_provinces(self):
        self.movc = Movc(1, 2017)
        self.movc.set_input_dir(self.input_dir)
        self.movc.set_output_dir(self.output_dir)
        mov_files = os.listdir(r"C:\Users\piepalla\PycharmProjects\new_movc\data\2017\01")
        self.logger.info(self.movc.get_missing_provinces(mov_files))
        self.movc1 = Movc(3, 2016)
        self.movc1.set_input_dir(self.input_dir)
        self.movc1.set_output_dir(self.output_dir)
        mov_files = os.listdir(r"C:\Users\piepalla\PycharmProjects\new_movc\data\2016\03")
        self.logger.info(self.movc.get_missing_provinces(mov_files))

    if __name__ == '__main__':
        unittest.main()