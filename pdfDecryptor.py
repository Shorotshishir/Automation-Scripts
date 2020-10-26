''' 
automate opening multiple pdf that is locked with password.
this script will open all the pdf with your secret_pass and
rewrite and save them without passwords.
keep this file in the pdf's directory.
'''

from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as read, \
    open(output_path, 'wb') as write:
    reader = PdfFileReader(read)
    reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))

    writer.write(write)

if __name__ == '__main__':
    secret_pass = 'set-your-pass-here'
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".pdf"):
            decrypt_pdf(filename, f'decrypted/{filename}.pdf', secret_pass)