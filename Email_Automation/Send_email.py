import win32com.client as wincl
from datetime import datetime

def main():
    outlook = wincl.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'your-email@example.com'
    mail.Subject = 'Main title of email'
    mail.Body = 'Hello\n\nThis is an automated email that contains important information, do not desregard this email. Thanks!'
    attachment = "C:\\Users\\userX\\Documents\\test" + str(datetime.now()).split(' ')[0] + ".xlsx"
    mail.Attachments.Add(attachment)
    mail.Send()

if __name__ == "__main__":
    main()