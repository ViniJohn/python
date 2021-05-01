import smtplib
import win32com.client as win32
import sys


outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'peter.vini@eplglobal.com'
mail.Subject = 'Rubella PO list '
mail.Body = ''' Hi Annia,
                    Please check the attachement.
            '''
mail.Send()