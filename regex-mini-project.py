import re


source_text = input("Please enter the source text: ")
regex_pattern = input("Please enter the pattern to find: ")

try:
    re.compile(regex_pattern)
    matched_string = re.findall(re.compile(regex_pattern), source_text)
    print(matched_string)
except re.error:
    print("Entered pattern is not valid")