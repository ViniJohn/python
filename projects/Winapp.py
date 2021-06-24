import tkinter as tk 
import time
import os
import win32com.client as win32
from datetime import date

class App(tk.Frame):
    def __init__(self, master):
        
        super().__init__(master)
        self.master.geometry("300x150")
        self.master.title("Plan it")
        self.master.resizable(0,0)
        self.app_widgets()
    
    def app_widgets(self):

        refplan_lblname = tk.Label(self.master , text="Refresh Plans")
        refplan_lblname.grid(row=0,column=0,sticky=tk.W,padx=5,pady=5)
        refplan_btn = tk.Button(self.master, text="Refresh",command=lambda:self.print_val())
        refplan_btn.grid(row=0,column=1,sticky=tk.E,padx=5,pady=5)
    
    def print_val(self):

        path = r"\\yourpath"
        file1_path = path +'\\'+list(filter(lambda x: "Excelwotkbook1" in x, os.listdir(path)))[0]
        file2_path = path +'\\'+list(filter(lambda x: "Excelwotkbook2" in x, os.listdir(path)))[0]

        xl = win32.DispatchEx('Excel.Application')
        xl.Application.visible = True
        wb = xl.Workbooks.Open(os.path.abspath(file1_path))
        xl.Application.run('\'' + file1_path.split('\\')[-1] + '\''+'!Module1.Excelwotkbook1macro')
        del xl
        del wb

        xl = win32.DispatchEx('Excel.Application')
        xl.Application.visible = True
        wb = xl.Workbooks.Open(os.path.abspath(file2_path))
        xl.Application.run('\'' + file2_path.split('\\')[-1] + '\''+'!Module1.Excelwotkbook1macro')
        del xl
        del wb
             

if __name__ == '__main__':
    root = tk.Tk()
    x = App(root)
    x.mainloop()