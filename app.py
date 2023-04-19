# importing required modules
from PyPDF2 import PdfReader

file_name = 'pdf/icagruppen-arsredovisning-2021.pdf'
 
# Creating a PDF reader object
reader = PdfReader(file_name)
 
print('\nPDF file:', file_name)
print('Pages:', len(reader.pages))

# creating a text variable to store the text extracted from the pdf
all_text = ''
# extracting text from each page
for page in reader.pages:
  all_text += page.extract_text()

# Print length
print('Length:', len(all_text))

# Print all lines of text that contains the word "scope" (case insensitive)
print('\nFinding “scope”:\n———————————————————————')
for line in all_text.splitlines():
  if 'scope' in line.lower():
    print(line)
print('———————————————————————')
