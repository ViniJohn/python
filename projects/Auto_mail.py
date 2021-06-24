import smtplib
import win32com.client as win32
import sys


outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'myemail@comapny.com'
mail.Subject = ' PO list '
mail.Body = ''' 
                    Please check the attachement.
            '''
mail.Send()