''' Author: Alejandro Bautista Ramos
    Last modification date: March 18th, 2018 '''

# Python 3.5.2 and above
# win32com comes from the pywin32 package version 223-cp35
import win32com.client as wincl
from subprocess import call
from datetime import datetime

def main():
	send_email()

def send_email():
	outlook      = wincl.Dispatch('outlook.application')
	mail         = outlook.CreateItem(0)
	mail.To      = 'destinataryemail@example.com'
	mail.Subject = 'Main Subject in Email'
	mail.Body    = 'Type in here the content of the email that will be read by your recipient.'
	attachment   = "C:\\Users\\userX\\Desktop\\file_to_be_attached.docx"
	mail.Attachments.Add(attachment)
	mail.Send()

def send_email_blat():
	'''How to use blat?

	1. Download blat from https://sourceforge.net/projects/blat/files/Blat%20Full%20Version/64%20bit%20versions/
	2. Extract the .zipped file
	3. Open CMD and see the different options by typing blat.exe /? (Remember that you need to be in the directory
	   where you downloaded blat.
	4. Set up the email that you will use to send emails by typing: Blat -install smtp.vcn.com name@example.com
    5. Send an email with blat directly in CMD by typing: blat test.txt -to name@example.com -subject "This is an
       automated email."
    6. Move the blat.dll and blat.exe files to a new path, in my case, C:\\blat_email
    7. Set up the template that will be used in your emails every time you send an automated email by creating a .txt file,
       i.e., mandatory_txt_file.txt. In this file you write what you want in your messages.
	8. Use the code from below to send the automated emails.
	'''

	date_of_xlsx = str(datetime.now()).split(' ')[0]
	blatstring = 'cmd  /cC:\\blat_email\\blat.exe C:\\blat_email\\mandatory_txt_file.txt -attach C:\\Users\\userX\\Documents\\test' + date_of_xlsx + '.xlsx -to your-email-goes-here -subject "Title of message goes here"'
	call(blatstring)


if __name__ == "__main__":
	main()
	