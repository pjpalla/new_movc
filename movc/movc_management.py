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
from movc.movxl import MovXL
from all7.all7_consts import *
from all7.all7 import All7
from ctt4.ctt4 import Ctt4
from ctt4.ctt4_consts import *
import re, os, locale, datetime, calendar


def menu():
    print("\n--- MOVC GENERATOR 2017 ---\n")
    print("* GENERATE MOVC       -----> (1)")
    print("* VALIDATE MOVC       -----> (2)")
    print("* LOAD MOVC FILE      -----> (3)")
    print("* EXPORT MOVC TO XL   -----> (4)")
    print("* GENERATE ALLEGATO 7 -----> (5)")
    print("* GENERATE CTT4       -----> (6)")
    print("* QUIT                -----> (0)")


def quit():
    return 0


def generate_movc():
    print("***** MOVC GENERATION PROCEDURE *****\n")
    province_name = ""
    year = None
    month = None
    while True:
        province_name = province_menu()
        if (province_name == False):
            return
        # province_name = input("Choose a Province [1-5]: \n\n"
        #                       "* CITTA' METROPOLITANA DI CAGLIARI -----> (1)\n"
        #                       "* PROVINCIA DEL SUD SARDEGNA       -----> (2)\n"
        #                       "* PROVINCIA DI ORISTANO            -----> (3)\n"
        #                       "* PROVINCIA DI NUORO               -----> (4)\n"
        #                       "* PROVINCIA DI SASSARI             -----> (5)\n"
        #                       "* QUIT                             -----> (0)\n\n"
        #                       " ----> ")
        #
        # province_name = check_province(province_name, get_value = True)


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
            if (check_province(province_name) & check_year(year) & check_month(month, year)):
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
    try:
        movc_filepath = movc_obj.create_movc(province_name)
    except Exception as e:
        print(e)
        return


    export = input("Do you want to export the file to EXCEL? [Y/N]")
    if re.search('[Yy]', export):
        xl_builder = MovXL(consts.XL_TEMPLATE_FILE, consts.MAPPING_FILE, movc_filepath)
        ### initial file name
        locale.setlocale(locale.LC_ALL, 'ita')
        month_name = (calendar.month_name[int(month)]).capitalize()
        province_symbol = province_data.PROVINCIAL_SYMBOLS[province_name]
        initial_filename = ("MOVC_" + province_symbol + "_" + month_name + "_" + year).upper()

        frame = Tk()
        filepath = asksaveasfilename(defaultextension='xlsx', initialfile=initial_filename)
        frame.destroy()
        print("\nExporting MOV/C to EXCEL\n....\n\n")
        xl_builder.build_xl(filepath)
        xl_builder.add_summary(filepath)
        print("...MOV/C successfully exported!")



def export_to_xl():
    print("***** EXPORT MOVC TO EXCEL *****\n")
    province_name = ""
    year = None
    month = None

    while True:
        province_name = province_menu()
        if (province_name == False):
            return
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
            if (check_province(province_name) & check_year(year) & check_month(month, year)):
                province_name = check_province(province_name, True)
                break
        elif re.search('^[Nn]', confirmation):
            continue
        else:
            return

    #output_dir = MovUtility.config_io_paths(year, month)[1]
    target_dir = MovUtility.default_io_config()[1]
    movc_to_convert = MovUtility.get_movc(target_dir, province_name, year, month)
    #print(movc_to_convert)
    xl_builder = MovXL(consts.XL_TEMPLATE_FILE, consts.MAPPING_FILE, movc_to_convert)

    ### initial file name
    locale.setlocale(locale.LC_ALL, 'ita')
    month_name = (calendar.month_name[int(month)]).capitalize()
    province_symbol = province_data.PROVINCIAL_SYMBOLS[province_name]
    initial_filename = ("MOVC_" + province_symbol + "_" + month_name + "_" + year).upper()

    frame = Tk()
    filepath = asksaveasfilename(defaultextension = 'xlsx', initialfile = initial_filename)
    frame.destroy()
    print("\nExporting MOV/C to EXCEL\n....\n\n")
    xl_builder.build_xl(filepath)
    xl_builder.add_summary(filepath)
    print("...MOV/C successfully exported!")



def validate_movc():
    print("***** MOVC VALIDATION PROCEDURE *****\n")
    province_name = ""
    year = None
    month = None

    while True:
        province_name = province_menu()
        if (province_name == False):
            return
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
            if (check_province(province_name) & check_year(year) & check_month(month, year)):
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
        province_name = province_menu(old = True)
        if (province_name == False):
            return
        #province_name = input("Province name: \n----> ")
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
            if (check_old_province(province_name) & check_year(year) & check_month(month, year)):
                province_name = check_old_province(province_name, True)
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
        '3': load_movc,
        '4': export_to_xl,
        '5': generate_allegato7,
        '6': generate_ctt4
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

def check_month(month, year):
    now = datetime.datetime.now()
    current_year, current_month = now.year, now.month
    try:
        if int(year) == current_year and  int(month) > current_month:
            print("\n**** Illegal value: [month] ****")
            print("**** Month selected can't be greater than current month ****\n")
            return False
        if int(month) in consts.ALLOWED_MONTHS:
            return True
        else:
            print("**** Illegal value: [month] ****")
            return False
    except:
        print("**** A problem has occurred.\nIllegal value: [month] ****")
        return False

def check_province(province, get_value=False):
    if (province == '1'):
        province = "cagliari"
    elif (province == '2'):
        province = "sud sardegna"
    elif (province == '3'):
        province = "oristano"
    elif (province == '4'):
        province = "nuoro"
    elif (province == '5'):
        province = "sassari"
    elif (province == '0'):
        province = 'quit'
    # if (re.search('citta|metropolitana|cagliari', province)):
    #     province = "cagliari"
    # elif (re.search('sud|sardegna', province)):
    #     province = "sud sardegna"

    if province in province_data.PROVINCIAL_SYMBOLS.keys():
        if get_value:
            return  province
        else:
            return True
    else:
        if province != 'quit':
            print("**** Illegal value: [province] ****")
        return False

def check_old_province(province, get_value = False):
    if (province == '1'):
        province = "cagliari"
    elif (province == '2'):
        province = "carbonia-iglesias"
    elif (province == '3'):
        province = "medio-campidano"
    elif (province == '4'):
        province = "oristano"
    elif (province == '5'):
        province = "nuoro"
    elif (province == '6'):
        province = 'ogliastra'
    elif (province == '7'):
        province = 'olbia-tempio'
    elif (province == '8'):
        province = 'sassari'
    elif (province == '0'):
        province = 'quit'
    # if (re.search('citta|metropolitana|cagliari', province)):
    #     province = "cagliari"
    # elif (re.search('sud|sardegna', province)):
    #     province = "sud sardegna"

    if province in province_data.OLD_PROVINCIAL_SYMBOLS.keys():
        if get_value:
            return  province
        else:
            return True
    else:
        if province != 'quit':
            print("**** Illegal value: [province] ****")
        return False

def province_menu(old = False):

     if old == True:
          province_name = input("Choose a Province [1-5]: \n\n"
          "* CAGLIARI                -----> (1)\n"
          "* CARBONIA-IGLESIAS       -----> (2)\n"
          "* MEDIO-CAMPIDANO         -----> (3)\n"
          "* ORISTANO                -----> (4)\n"
          "* NUORO                   -----> (5)\n"
          "* OGLIASTRA               -----> (6)\n"
          "* OLBIA-TEMPIO            -----> (7)\n"
          "* SASSARI                 -----> (8)\n\n"
          " ----> ")
     else:
          province_name = input("Choose a Province [1-5]: \n\n"
          "* CITTA' METROPOLITANA DI CAGLIARI -----> (1)\n"
          "* PROVINCIA DEL SUD SARDEGNA       -----> (2)\n"
          "* PROVINCIA DI ORISTANO            -----> (3)\n"
          "* PROVINCIA DI NUORO               -----> (4)\n"
          "* PROVINCIA DI SASSARI             -----> (5)\n"
          "* QUIT                             -----> (0)\n\n"
          " ----> ")
     if (old == True):
         province_name = check_old_province(province_name, get_value=True)
     else:
        province_name = check_province(province_name, get_value=True)
     return(province_name)

def generate_allegato7():
    print("***** ALLEGATO 7 GENERATION *****\n")
    province_name = ""
    year = None
    month = None
    while True:
        province_name = province_menu()
        if (province_name == False):
            return
        print(province_name)
        year = input("\nYear [2016 - ]: \n----> ")
        print("\n*******************************************")
        print('Data inserted:')
        print("\nProvince:", province_name)
        print("\nYear: ", year)
        print("*********************************************\n")
        confirmation = input("Confirm?[Yes/No/Quit]\n---->")
        if re.search('^[Yy]', confirmation):
            if (check_province(province_name) & check_year(year)):
                break
        elif re.search('^[Nn]', confirmation):
            continue
        else:
            return
    province_extended = ""
    if (province_name == 'sud sardegna'):
        province_extended = "sud_sardegna"
    else:
        province_extended = province_name

    base_dir = MovUtility.get_all7_base_dir()
    input_dir = os.path.join(base_dir, year, province_extended)
    output_dir =  os.path.join(base_dir, year, "output")
    output_file = os.path.join(output_dir, ALL7_BASE_OUTPUT + province_extended + "_" + year + ALL7_EXT)
    # print(input_dir)
    # print(output_dir)
    # print(output_file)
    # print(os.listdir(input_dir))
    all7 = All7(ALL7_TEMPLATE_PATH, year, province_name)
    print("Generating Allegato 7.....\n")
    print("...the operation can take a few minutes ...")
    try:
       all7.build_xl(input_dir, output_file)
    except Exception as e:
        print("A problem has occurred! The Allegato 7 generation process failed!\n")
    finally:
        return


def generate_ctt4():
    print("***** CTT4 GENERATION *****\n")
    province_name = ""
    year = None

    while True:
        province_name = province_menu()
        if (province_name == False):
            return
        print(province_name)
        year = input("\nYear [2017 - ]: \n----> ")
        print("\n*******************************************")
        print('Data inserted:')
        print("\nProvince:", province_name)
        print("\nYear: ", year)
        print("*********************************************\n")
        confirmation = input("Confirm?[Yes/No/Quit]\n---->")
        if re.search('^[Yy]', confirmation):
            if (check_province(province_name) & check_year(year)):
                break
        elif re.search('^[Nn]', confirmation):
            continue
        else:
            return
    province_extended = ""
    # if (province_name == 'sud sardegna'):
    #     province_extended = "sud_sardegna"
    # else:
    province_extended = province_name


    base_dir = MovUtility.get_ctt4_base_dir()
    input_dir = os.path.join(base_dir, "input")
    output_dir =  os.path.join(base_dir, "output")

    ctt4 = Ctt4(TEMPLATE_PATH, MAPPING_PATH, year, province_extended)


    print("Generating CTT4.....\n")
    print("...the operation can take a few minutes ...")
    try:
        ctt4.build_ctt4(province_extended, year, input_dir, output_dir)
        print("The operation completed successfully!")
    except Exception as e:
        print("A problem has occurred! The CTT4 generation process failed!\n")
    finally:
        return





if __name__ == "__main__":
    main(sys.argv)