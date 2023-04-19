# importing required modules
from PyPDF2 import PdfReader
 
# creating a pdf reader object
reader = PdfReader('pdf/icagruppen-arsredovisning-2021.pdf')
 
# printing number of pages in pdf file
print('\nPages:', len(reader.pages))

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
