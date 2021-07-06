import win32com.client as win32
import os

from win32com.client.genpy import MakeEventMethodName 

class MailSender():
        def __init__(self):
            self.send_mail = win32.Dispatch("outlook.application").CreateItem(0)
            self.read_inbox = win32.Dispatch("outlook.application").GetNamespace("MAPI").GetDefaultFolder(6) 

        def send_mail(self):
                pass

        def send_mailwithatt(self):
                pass

        @staticmethod   
        def email_list():
                curr_path = os.path.dirname(os.path.realpath(__file__))
                with open(curr_path+'\emaillist.txt') as mail_list:
                        return [x.replace('\n','') for x in mail_list.readlines()]

# outlook = win32.Dispatch('outlook.application')
# mail = outlook.CreateItem(0)
# mail.To = 'peter.vini@eplglobal.com;vinijaimarsaline@gmail.com'
# mail.Subject = ' PO list '
# mail.Body = ''' 
#                     Please check the attachement.
#             '''
# mail.Send()

a = MailSender()        
message = a.read_inbox.Items
vmi = message.Restrict(f"[Subject] = 'VMI upload WK27 06.07.2021'")
for mes in vmi:
        for attachment in mes.Attachments:
                if "upload" in attachment.FileName:
                        attachment.SaveAsFile(os.path.join(r"C:\Users\peter.vini\Desktop",attachment.FileName))
                        print('soemthing')
                else:
                        print("nothing")