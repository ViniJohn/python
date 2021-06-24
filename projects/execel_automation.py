import os
import win32com.client as win32

path=r"Filepath"

def run_macro (path):
    file1_path = path +'\\'+list(filter(lambda x: "myexcelworkbook" in x, os.listdir(path)))[0]
    xl = win32.DispatchEx('Excel.Application')
    xl.Application.visible = True
    wb = xl.Workbooks.Open(os.path.abspath(file1_path))
    xl.Application.run('\'' + file1_path.split('\\')[-1] + '\''+'!Module1.macro')
    del xl
    del wb
