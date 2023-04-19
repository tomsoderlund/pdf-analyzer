import nltk
from sklearn.model_selection import train_test_split

from pdf_text import get_interesting_text_from_pdf
from string_helpers import preprocess_numbers
import dummy_values

file_name = 'pdf/icagruppen-arsredovisning-2021.pdf'
search_term = 'scope'

#interesting_text = dummy_values.interesting_text
interesting_text = get_interesting_text_from_pdf(file_name, search_term)

# Remove spaces as thousand separators
interesting_text_numbers = preprocess_numbers(interesting_text)

# Split the text into sentences and tokenize each sentence into words
nltk.download('punkt')
sentences = nltk.sent_tokenize(interesting_text_numbers)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
#print(tokenized_sentences)

# Divide the tokenized sentences into training and validation sets
training_sentences, validation_sentences, training_labels, validation_labels = train_test_split(tokenized_sentences, [0] * len(tokenized_sentences), test_size=0.25, random_state=1000)
print([training_sentences, validation_sentences, training_labels, validation_labels])
