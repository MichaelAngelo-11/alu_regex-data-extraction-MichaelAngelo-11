from extractors.regex_extractors import *

with open("data_samples/test_strings.txt", "r") as f:
    text = f.read()

print("== Extracted Results ==")
print("Emails:", extract_emails(text))
print("URLs:", extract_urls(text))
print("Phone Numbers:", extract_phone_numbers(text))
print("Credit Cards:", extract_credit_cards(text))
print("Times:", extract_time_formats(text))
print("Hashtags:", extract_hashtags(text))
