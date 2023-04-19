import re

# Remove spaces as thousand separators
def preprocess_numbers(text):
    # Regular expression pattern to find numbers with spaces as thousand separators
    pattern = r'(\d{1,3}(?:\s\d{3})+(?:(?:\.\d+)|(?:,\d+))?)'

    # Function to replace spaces with non-breaking space characters
    def replace_spaces(match):
        number = match.group(0)
        return number.replace(' ', '')

    # Replace spaces with non-breaking space characters in the numbers found
    processed_text = re.sub(pattern, replace_spaces, text)
    return processed_text
