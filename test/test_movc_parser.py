__author__ = 'pg'
import unittest
import logging
from movc.movc_parser import MovcParser
from movc.consts import *
import pandas as pd
from movc.movc_fields import *

class TestMovcParser(unittest.TestCase):
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

        movc_path = r"C:\Users\piepalla\PycharmProjects\new_movc\output\2016\01\movc_ca_012016.txt"
        movc_path2 = r"C:\Users\piepalla\PycharmProjects\new_movc\output\2016\01\movc_ss_012016.txt"

        self.parser = MovcParser(movc_path, MAPPING_FILE)
        self.parser1 = MovcParser(movc_path2, MAPPING_FILE)
        self.parser.open_session()


    def tearDown(self):
        self.parser = None
        # self.parser.close_session()

    def test_get_movc_blocks(self):
        blocks = self.parser.get_movc_blocks()
        self.assertEqual(17, len(blocks))
        self.logger.info(blocks[0][0][8:13])
        blocks1 = self.parser1.get_movc_blocks()
        self.assertEqual(68, len(blocks1))


    def test_get_year(self):
        blocks = self.parser.get_movc_blocks()
        year = self.parser.get_year(blocks[17])
        self.assertEqual('2016', year)

    def test_get_month(self):
        blocks = self.parser.get_movc_blocks()
        month = self.parser.get_month(blocks[7])
        self.assertEqual(month, '1')
        self.assertIsInstance(month, str)

    def test_get_provincia(self):
        blocks = self.parser.get_movc_blocks()
        block1 = blocks[0]
        block2 = blocks[1]
        self.logger.info(self.parser.get_comune(block1)[0])
        self.logger.info(self.parser.get_province(block1))

    def test_get_comune(self):
        blocks = self.parser.get_movc_blocks()
        block1 = blocks[0]
        block2 = blocks[1]
        self.logger.info(self.parser.get_comune(block1)[0])
        self.assertEqual("Assemini", self.parser.get_comune(block1)[0])
        self.logger.info(self.parser.get_comune(block2))

    def test_get_comune2(self):
        movc_path = r"C:\Users\piepalla\PycharmProjects\new_movc\output\2017\01\movc_ca_012017.txt"

        self.parser = MovcParser(movc_path, MAPPING_FILE)
        self.parser.open_session()
        blocks = self.parser.get_movc_blocks()
        for b in blocks:
            self.logger.info(self.parser.get_comune(b)[0])

    def test_get_tipo_localita_turistica(self):
        pass



    def test_get_structure(self):
        blocks = self.parser1.get_movc_blocks()
        line1 = blocks[1][0]
        type = "A1"
        field = self.parser1.get_structure(type, line1)
        self.assertEqual(field, 2)

        line2 = blocks[1][1]
        field = self.parser1.get_structure(type, line2)
        self.assertEqual(field, 266)
        type = "A2"
        line1 = blocks[1][0]
        field = self.parser1.get_structure(type, line1)
        self.assertEqual(field, 15)


    def test_get_capacity(self):
        blocks = self.parser1.get_movc_blocks()
        block2 = blocks[1]
        esercizi = self.parser1.get_capacity(CAPACITY['esercizi'], block2)
        letti = self.parser1.get_capacity(CAPACITY['letti'], block2)
        camere = self.parser1.get_capacity(CAPACITY['camere'], block2)
        bagni = self.parser1.get_capacity(CAPACITY['bagni'], block2)
        letti_aperti = self.parser1.get_capacity(CAPACITY['letti negli esercizi aperti'], block2)
        letti_esercizi_aperti_rispondenti = self.parser1.get_capacity(CAPACITY['letti negli esercizi aperti rispondenti'], block2)
        giornate_letto = self.parser1.get_capacity(CAPACITY['giornate letto disponibili'], block2)
        giornate_camere = self.parser1.get_capacity(CAPACITY['giornate camere disponibili'], block2)
        giornate_camere_occupate = self.parser1.get_capacity(CAPACITY['giornate camere occupate'], block2)
        self.logger.info(esercizi)
        self.logger.info(letti)
        self.logger.info(camere)
        self.logger.info(bagni)
        self.logger.info(letti_aperti)
        self.logger.info(letti_esercizi_aperti_rispondenti)
        self.logger.info(giornate_letto)
        self.logger.info(giornate_camere)
        self.logger.info(giornate_camere_occupate)
        self.assertEqual(19, len(esercizi))


    def test_get_esercizi(self):
        blocks = self.parser.get_movc_blocks()
        for b in blocks:
            esercizi = self.parser.get_esercizi(b)
            self.assertEqual(20, len(esercizi))
        blocks = self.parser1.get_movc_blocks()
        block2 = blocks[1]
        esercizi = self.parser1.get_esercizi(block2)
        self.assertEqual(2, esercizi[0])
        self.assertEqual(15, esercizi[1])
        self.assertEqual(5, esercizi[5])
        self.logger.info(esercizi)

    def test_get_arrivals_presences_by_structure(self):
        blocks = self.parser.get_movc_blocks()
        line = blocks[0][57]
        self.logger.info(line)
        type = "C1"
        arrivals, presences = self.parser.get_arrivals_presences_by_structure(type, line)
        self.assertEqual(1, arrivals)
        self.assertEqual(1, presences)

        line = blocks[0][59]
        type = "A7"
        arrivals, presences = self.parser.get_arrivals_presences_by_structure(type, line)
        self.assertEqual(73, arrivals)
        self.assertEqual(155, presences)

    def test_get_movements(self):
        blocks = self.parser.get_movc_blocks()
        capacity = self.parser.get_capacity('004', blocks[0])
        movements = self.parser.get_movements('007', blocks[0])

        self.logger.info(capacity)
        self.logger.info(movements)
        self.assertEqual(19, len(capacity))
        self.assertEqual(19, len(movements))



    def test_compute_extra_total(self):
        blocks = self.parser.get_movc_blocks()
        line = blocks[0][73]
        self.logger.info(line)
        arrivals, presences = self.parser.compute_extra_total(line)
        self.assertEqual(2, arrivals)
        self.assertEqual(2, presences)
        line = blocks[2][9]
        self.logger.info(line)
        comune = self.parser.get_comune(blocks[2])
        self.logger.info(comune)
        arrivals, presences = self.parser.compute_extra_total(line)
        # self.logger.info(arrivals)
        # self.logger.info(presences)
        self.assertEqual(0, arrivals)
        self.assertEqual(0, presences)
        line = blocks[2][77]
        self.logger.info(line)
        arrivals, presences = self.parser.compute_extra_total(line)
        self.assertEqual(7, arrivals)
        self.assertEqual(7, presences)


    def test_compute_extra_total2(self):
        blocks = self.parser.get_movc_blocks()
        line = blocks[0][0]
        self.logger.info(line)
        tot_esercizi_extra = self.parser.compute_extra_total(line)
        self.assertEqual(10, tot_esercizi_extra)
        line = blocks[0][1]
        self.logger.info(line)
        tot_letti_extra = self.parser.compute_extra_total(line)
        self.assertEqual(108, tot_letti_extra)
        line = blocks[0][2]
        self.logger.info(line)
        tot_camere_extra = self.parser.compute_extra_total(line)
        self.assertEqual(54, tot_camere_extra)
        line = blocks[0][3]
        self.logger.info(line)
        tot_bagni_extra = self.parser.compute_extra_total(line)
        self.assertEqual(10, tot_bagni_extra)

    # def test_getA1(self):
    #     blocks = self.parser1.get_movc_blocks()
    #     line = blocks[4][0]
    #     a1 = self.parser1.getA1(line)
    #     self.logger.info(a1)


    # def test_get_comuni(self):
    #     block = self.parser.get_movc_block(1, 90)
    #     codice_comune, nome_comune = self.parser.get_comune(block)
    #     self.logger.info(codice_comune)
    #     self.logger.info(nome_comune)
    #     self.assertEqual(codice_comune, '92003')
    #     self.assertEqual(nome_comune, 'Assemini')
    #     new_block = self.parser.get_movc_block(91, 180)
    #     self.assertEqual(len(new_block), 90)

        #self.logger.info(new_block[0])
        # codice_comune, nome_comune = self.parser.get_comune(block)
        # self.assertEqual(codice_comune, '92009')
        # self.logger.debug(mapper[['com_new', 'com_name']][1:4])
        #
        # self.logger.debug(mapper.loc[mapper['com_new'].isin(codici_comuni)])
        # m = mapper['com_name'].loc[mapper['com_new'].isin(codici_comuni)]
        # self.logger.debug(mapper['com_name'].loc[mapper['com_new'].isin(codici_comuni)])
        # self.logger.debug(m.tolist())

        # comuni_nomi = mapper['com_name']
        # df = pd.DataFrame(index=comuni,data=comuni_nomi, columns=['com_name'])
        # self.logger.debug(df)
        # # self.logger.debug(comuni)
       # self.logger.debug(mapper.com_name)
        # self.logger.debug(mapper[['com_new', 'com_name']])
        # m = mapper[['com_new', 'com_name']]
        # self.logger.debug(m)
