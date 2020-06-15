import PyPDF2
import sys
import smtplib
from email.message import EmailMessage

#take all argument from terminal
inputs = sys.argv[1:]
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
newPdf = PyPDF2.PdfFileWriter()

merger = PyPDF2.PdfFileMerger()
for pdf in inputs:
	#watermark the pdf page
	nameOfPdf = PyPDF2.PdfFileReader(open(pdf, 'rb'))
	for i in range(nameOfPdf.getNumPages()):
		page = nameOfPdf.getPage(i)
		page.mergePage(watermark.getPage(0))
		newPdf.addPage(page)

	#append all Pdfs in one pdf
	with open('new_pdf.pdf', 'wb') as file:
		newPdf.write(file)
		print('all good')

#now sending the pdf
email = EmailMessage()
email['from'] = 'Asmaa O'
email['to'] = 'write the gmail '
email['subject'] = 'You won 1,000,000 dollars! :D'

email.set_content('I am a Python master! *-*')
with open('new_pdf.pdf', 'rb') as att_pdf:
	att = att_pdf.read()
	email.add_attachment(att, maintype='application/pdf', subtype='pdf', filename='new_pdf.pdf')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('Your gmail', 'Ur password')
	smtp.send_message(email)
	print('all good boss!')


