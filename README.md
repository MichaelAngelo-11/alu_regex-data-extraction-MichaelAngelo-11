# Regex Data Extraction

This project extracts structured data like emails, URLs, phone numbers, and more from raw text using Python and regular expressions. It was built as part of a junior full-stack development project.

## Extracted Data Types

- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Time formats (12-hour and 24-hour)
- Hashtags

## Sample Input (`data_samples/test_strings.txt`)

Emails: user@example.com, firstname.lastname@company.co.uk
URLs: https://www.example.com, https://subdomain.example.org/page
Phone Numbers: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Times: 14:30, 2:30 PM, 9:45 am, 23:59
Hashtags: #example, #ThisIsAHashtag


## Sample Output (Console)

Run `python3 extractors/regex_extractors.py` and see:

Emails: ['user@example.com', 'firstname.lastname@company.co.uk']
URLs: ['https://www.example.com', 'https://subdomain.example.org/page']
Phone Numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
Credit Cards: ['1234 5678 9012 3456', '1234-5678-9012-3456']
Times: ['14:30', '2:30 PM', '9:45 am', '23:59']
Hashtags: ['#example', '#ThisIsAHashtag']

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/MichaelAngelo-11/alu_regex-data-extraction-MichaelAngelo-11.git
cd alu_regex-data-extraction-MichaelAngelo-11
### 2. Run the script


python3 extractors/regex_extractors.py

No external libraries required — works with a standard Python installation

### Project Structure


alu_regex-data-extraction-MichaelAngelo-11/
├── extractors/
│   └── regex_extractors.py
├── data_samples/
│   └── test_strings.txt
├── tests/
│   └── test_extractors.py
├── README.md
