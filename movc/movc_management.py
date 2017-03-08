__author__ = 'pg'

import sys
import time
import shutil
import pdb

from tkinter.filedialog import *
from movc import consts
from movc import province_data
from movc.movutility import MovUtility
from movc.new_movc import Movc
import re, os


def menu():
    print("\n--- MOVC GENERATOR 2017 ---\n")
    print("* GENERATE MOVC  -----> (1)")
    print("* VALIDATE MOVC  -----> (2)")
    print("* LOAD MOVC FILE -----> (3)")
    print("* QUIT           -----> (0)")




def quit():
    return 0

def generate_movc():
    print("***** MOVC GENERTATION PROCEDURE *****\n")
    province_name = ""
    year = None
    month = None

    while True:
        province_name = input("Province name: \n----> ")
        year = input("\nYear [2016 - ]: \n----> ")
        month = input("\nMonth [1-12]: \n----> ")
        print("\n*******************************************")
        print('Data inserted:')
        print("\nProvince:", province_name)
        print("\nYear: ", year)
        print("\nMonth: ", month)
        print("*********************************************\n")
        confirmation = input("Confirm?[Yes/No/Quit]\n---->")
        if re.search('^[Yy]', confirmation):
            if (check_province(province_name) & check_year(year) & check_month(month)):
                break
        elif re.search('^[Nn]', confirmation):
            continue
        else:
            return
    ### New Mov/c generation ###

    input_path, output_path =  MovUtility.default_io_config()
    # input_path, output_path = MovUtility.config_io_paths(year, month)
    # merged_file = MovUtility.get_merged_file(year, month)
    # # print("\nMerging old movc modules...")
    # MovUtility.merge_movs(year,month)
    # print("...done!\n")
    print("\n************************")
    time.sleep(2)

    movc_obj = Movc(month, year)
    movc_obj.set_input_dir(input_path)
    movc_obj.set_output_dir(output_path)
    movc_obj.set_mapper(consts.MAPPING_FILE)
    movc_obj.create_movc(province_name)


def validate_movc():
    print("***** MOVC VALIDATION PROCEDURE *****\n")
    province_name = ""
    year = None
    month = None

    while True:
        province_name = input("Province name: \n----> ")
        #province_name = check_province(province_name)
        year = input("\nYear [2016 - ]: \n----> ")
        #year = check_year(year)
        month = input("\nMonth [1-12]: \n----> ")
        #month = check_month(month)
        print("\n********************************************")
        print('Data inserted:')
        print("\nProvince:", province_name)
        print("\nYear: ", year)
        print("\nMonth: ", month)
        print("*********************************************\n")
        confirmation = input("Confirm?[Yes/No/Quit]\n----> ")

        if re.search('^[Yy]', confirmation):
            if (check_province(province_name) & check_year(year) & check_month(month)):
                province_name = check_province(province_name, True)
                break
        elif re.search('^[Nn]', confirmation):
            continue
        else:
            return

    #output_dir = MovUtility.config_io_paths(year, month)[1]
    input_dir, output_dir = MovUtility.default_io_config()
    movc_obj = Movc(month, year)
    movc_obj.set_mapper(consts.MAPPING_FILE)
    movc_obj.set_input_dir(input_dir)
    movc_obj.set_output_dir(output_dir)
    movc_file = MovUtility.get_movc(movc_obj.get_output_dir(), province_name, year, month)
    movc_obj.validate(movc_file)



def load_movc():
    print("***** LOADING OLD MOVC MODEL *****\n")
    filepath = None
    destination_path = None
    while True:
        province_name = input("Province name: \n----> ")
        #province_name = check_province(province_name)
        year = input("Year [2016 - ]: \n----> ")
        #year = check_year(year)
        month = input("Month [1-12]: \n----> ")
        #filepath = input("File to upload [path]: \n----> ")
        ## Opening file dialog box ###
        print("\nUploading Movc .....")
        frame = Tk()
        filepath = askopenfilename()
        ### closing file dialog
        frame.destroy()
        print("... Done!\n")
        #######
        if not os.path.exists(filepath):
            print(" **** File not found: {0} ****".format(filepath))
            return
        print("\n*******************************************")
        print('Data inserted:')
        print("\nProvince:", province_name)
        print("\nYear: ", year)
        print("\nMonth: ", month)
        print("*********************************************\n")
        confirmation = input("Confirm?[Yes/No/Quit]\n----> ")

        if re.search('^[Yy]', confirmation):
            if (check_province(province_name) & check_year(year) & check_month(month)):
                province_name = check_province(province_name, True)
            else:
                return
        elif re.search('^[Nn]', confirmation):
            continue
        else:
            return


        input_dir = MovUtility.default_io_config()[0]
        destination_path = MovUtility.get_movc(input_dir, province_name, year, month)
        if os.path.exists(destination_path):
            answer = input("\nA MOVC for the province selected is already present.\nDo you want to overwrite it? [Yes/No/Quit]\n----> ")
            if re.search('^[Yy]', answer):
                break
            elif re.search('^[Nn]]', answer):
                continue
            else:
                return
        else:
            break

    shutil.copyfile(filepath, destination_path)
    print("\n**** Upload successfully completed! **** ")




def main(argv):
    commands = {
        '0': quit,
        '1': generate_movc,
        '2': validate_movc,
        '3': load_movc
    }
    while True:
        menu()
        option_selected = input("\nSELECT ----> ")
        if option_selected not in commands.keys():
            print("\n ** WRONG OPTION: COMMAND NOT FOUND!! **\n")
            continue
        print(option_selected)
        res = commands[str(option_selected)]()
        if res == 0:
            break

def check_year(year):
    try:
       if int(year) in consts.ALLOWED_YEARS:
           return True
       else:
           print("**** Illegal value: [year] ****")
           return False
    except:
        print("**** Illegal value: [year] ****")
        return False

def check_month(month):
    try:
        if int(month) in consts.ALLOWED_MONTHS:
            return True
        else:
            print("**** Illegal value: [month] ****")
            return False
    except:
        print("**** Illegal value: [month] ****")
        return False

def check_province(province, get_value = False):
    if (re.search('città|metropolitana|cagliari', province)):
        province = "cagliari"
    elif (re.search('sud|sardegna', province)):
        province = "sud sardegna"

    if province in province_data.PROVINCIAL_SYMOBOLS.keys():
        if get_value:
            return  province
        else:
            return True
    else:
        print("**** Illegal value: [province] ****")
        return False






if __name__ == "__main__":
    main(sys.argv)