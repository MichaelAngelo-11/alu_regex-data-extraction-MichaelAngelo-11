# extractors/regex_extractors.py

import re

def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?"
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)

def extract_credit_cards(text):
    pattern = r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
    return re.findall(pattern, text)

def extract_time_formats(text):
    pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b"
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r"#\w+"
    return re.findall(pattern, text)

# Example runner (for debugging)
if __name__ == "__main__":
    with open("data_samples/test_strings.txt", "r") as file:
        data = file.read()
    
    print("Emails:", extract_emails(data))
    print("URLs:", extract_urls(data))
    print("Phones:", extract_phone_numbers(data))
    print("Cards:", extract_credit_cards(data))
    print("Times:", extract_time_formats(data))
    print("Hashtags:", extract_hashtags(data))
