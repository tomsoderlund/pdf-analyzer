from PyPDF2 import PdfReader

# Function to extract text from a PDF file given a search_term
def get_interesting_text_from_pdf(file_name, search_term):
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
  interesting_text = ''
  for line in all_text.splitlines():
    if search_term in line.lower():
      interesting_text += line + '\n'
  print('\nFinding “', search_term, '”:\n———————————————————————\n', interesting_text, '———————————————————————\n')
  return interesting_text
