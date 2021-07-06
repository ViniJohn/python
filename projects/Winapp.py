import re, os ,configparser,time
import tkinter as tk
import win32com.client as win32

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.app_widgets()
        self.statusbar()


    def app_widgets(self):
        '''UI widgets creation & function assigning'''
        self.master.geometry("300x300")
        self.master.title("Plan it")
        self.master.resizable(0,0)
        # setting Grid size
        self.grid_size = 0
        while self.grid_size <4:
            self.master.rowconfigure(self.grid_size,weight=1)
            self.master.columnconfigure(self.grid_size,weight=1)
            self.grid_size += 1             
        #var_widget 'checkbuttonname' : [fncbuttonname,fnc]
        self.plan = tk.BooleanVar()
        self.vmi = tk.BooleanVar()
        self.pwo = tk.BooleanVar()
        self.var_widget = {'Refresh Plans' :['Refresh',self.ref_macro,self.plan],
                           'VMI analysis':['Send',self.send_vmi,self.vmi],
                           'PWO confirmation':['send',self.send_pwoconfirmation,self.pwo]}  
        #Creating Widgets 
        g_r = 0
        g_c = 0 
        for k,v in self.var_widget.items():
            tk.Checkbutton(self.master,text=k,variable=v[2],onvalue=True,offvalue=False,anchor='nw',justify='left')\
                .grid(row =g_r,column=g_c,ipadx=10)
            tk.Button(self.master,text=v[0],command=v[1])\
                .grid(row=g_r,column=g_c+1,ipadx=30)
            g_r +=1 
        #statusbar
        self.status_val = tk.Label(self.master,text='Status..',borderwidth=2,relief='solid',anchor='w',justify=tk.LEFT)
        self.status_val.grid(row=self.grid_size,column=0,columnspan=self.grid_size,ipadx=100,sticky=(tk.N,tk.E,tk.W,tk.S))
        
    def statusbar(self,Stext=None):        
        #status bar update
        self.status_val.config(text =Stext)

    def ref_macro(self):
        '''Funtion to call macros from excel using win32 module
            Delcaring excel file Path , Plan and macro from Ref:config_read()fucntion below 
        '''
        if self.plan.get():
            config_section = 'excel'
            path   = self.config_read(config_section)['path']
            plans  = [self.config_read(config_section)['excel1'],self.config_read(config_section)['excel2']]        
            for excel,module in plans:
                excel_path = path +'\\'+list(filter(lambda x: excel in x, os.listdir(path)))[0]
                xl = win32.DispatchEx('Excel.Application')
                xl.Application.visible = True
                wb = xl.Workbooks.Open(os.path.abspath(excel_path))
                xl.Application.run('\'' + excel_path.split('\\')[-1] + '\''+module)
                del xl
                del wb
            self.statusbar('Plans refreshed' )
        return self.statusbar('Please select Refresh plan checkbox')
    
    def send_vmi(self):
        if self.vmi.get():

            self.statusbar('VMI analysis sent')
        return self.statusbar('Please select VMI plan checkbox')

    def send_pwoconfirmation(self):
        if self.pwo.get():

            self.stautsbar('PWO confimation sent')
        return self.statusbar('Please check the PWO Confirmation check box')
             
    @staticmethod
    def config_read(fnc_variable):
        '''
        Returns dic which contains path ,Plan1 and plan2 as list of execel workbook with module 
        Example config file
        [excel]
        path = youfilepath
        excel1 = yourPlan1
        excel2 = yourPlan2
        excel1_Module = Module1
        excel2_Module = Module2
        '''
        config = configparser.ConfigParser()
        config.read(os.path.dirname(os.path.realpath(__file__))+'\\config.ini')
    
        if fnc_variable == 'excel':
            return {'path'   :   config['excel']['path'],
                    'excel1'  :   [config['excel']['excel1'],config['excel']['excel1_Module']],
                     'excel2'  :   [config['excel']['excel2'],config['excel']['excel2_Module']]}
         
        if fnc_variable == 'sql':
            return {'server' : config['sql']['server'],
                    'database' :config['sql']['database'],
                    'username' :config['sql']['username'],
                    'password' : config['sql']['password']
                    }
          
if __name__ == '__main__':
    root = tk.Tk()
    x = App(root)
    x.mainloop()

