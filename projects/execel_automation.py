import os
import win32com.client as win32
import time 

def run_excel_macro (file_path, separator_char):
    """
    Execute an Excel macro
    :param file_path: path to the Excel file holding the macro
    :param separator_char: the character used by the operating system to separate pathname components
    :return: None
    """
    xl = win32.DispatchEx('Excel.Application')
    xl.Application.visible = True
    wb = xl.Workbooks.Open(os.path.abspath(file_path))
    print(file_path.split(sep=separator_char)[-1] + "!Module6.ToRefPlan")
    #xl.Application.run(file_path.split(sep=separator_char)[-1] + "!Module14.refall")
    wb.Save()
    xl.Application.Quit()
    del xl

separator_char = os.sep
run_excel_macro(r"C:\Users\peter.vini\Desktop\PrintingFreezePlan04Mayof2021.xlsm", separator_char)

