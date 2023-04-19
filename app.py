# importing required modules
from PyPDF2 import PdfReader
import nltk

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
SEARCH_TERM = 'scope'
interesting_text = ''
for line in all_text.splitlines():
  if SEARCH_TERM in line.lower():
    interesting_text += line + '\n'
print('\nFinding “', SEARCH_TERM, '”:\n———————————————————————\n', interesting_text, '———————————————————————\n')

# Split the text into sentences and tokenize each sentence into words
nltk.download('punkt')
sentences = nltk.sent_tokenize(interesting_text)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
print(tokenized_sentences)
