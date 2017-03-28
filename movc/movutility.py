__author__ = 'pg'
import os
from os.path import *
import glob
from movc import province_data
from movc.exceptions import IllegalArgumentError
from tkinter.filedialog import *


class MovUtility:

    @staticmethod
    def default_io_config():
        base_dir = dirname(dirname(realpath(__file__)))
        base_input_dir = "data"
        base_output_dir = "output"
        input_dir = os.path.join(base_dir, base_input_dir)
        output_dir = os.path.join(base_dir, base_output_dir)
        return input_dir, output_dir


    @staticmethod
    def set_io_config():
        pass



    @staticmethod
    def config_io_paths(year, month):
        base_dir = dirname(dirname(realpath(__file__)))
        base_input_dir = "data"
        base_output_dir = "output"
        m = str(month)
        y = str(year)

        if len(m) == 1:
            m = '0' + m

        input_dir = os.path.join(base_dir, base_input_dir, y, m)
        output_dir = os.path.join(base_dir, base_output_dir, y, m)
        return input_dir, output_dir


    @staticmethod
    def get_merged_file(year, month):
        ### target dir ###
        base_dir = dirname(dirname(realpath(__file__)))
        base_input_dir = "data"
        year = str(year)
        month = str(month)
        if len(month) == 1:
            month = '0' + month

        target_dir = os.path.join(base_dir, base_input_dir, year, month)
        merged_filename = "all_" + month + year + ".txt"
        return os.path.join(target_dir, merged_filename)


    @staticmethod
    def build_out_filename(filepath):
        basename = "all_"
        time_ref = (os.path.basename(filepath).split(sep='_')[-1]).split('.')[0]
        return basename + time_ref + ".txt"


    @staticmethod
    def get_movc(base_dir, province_name, year, month):
        province_symbol = None
        if province_name.lower() in province_data.PROVINCIAL_SYMBOLS.keys():
            province_symbol = province_data.PROVINCIAL_SYMBOLS[province_name.lower()]
        else:
            raise IllegalArgumentError("Invalid province name")

        year = str(year)
        month = str(month)
        if len(month) == 1:
            month = '0' + month

        movc_dir = os.path.join(base_dir, year, month)
        output_base_filename = "movc_" + province_symbol + "_" + month + year + ".txt"
        file_path = os.path.join(movc_dir, output_base_filename)
        return file_path