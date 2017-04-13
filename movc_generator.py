__author__ = 'pg'
from  movc.new_movc import *
from movc.movutility import *
from movc import consts

import sys

if (len(sys.argv) < 2):
    print("Wrong number of arguments")
    sys.exit()


input_path, output_path = MovUtility.default_io_config()

month, year = 3, 2016

movc_obj = Movc(month, year)
movc_obj.set_input_dir(input_path)
movc_obj.set_output_dir(output_path)
movc_obj.set_mapper(consts.MAPPING_FILE)

movc_filepath = movc_obj.create_movc("cagliari")

movc_filepath