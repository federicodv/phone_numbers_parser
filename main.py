import os
import re

def parse_number(phone_number, country=7, area=812):
    phone_number = "".join(re.findall('[0-9]', phone_number))
    if len(phone_number) <= 11 and len(phone_number) > 6: 
        if len(phone_number) == 11 or len(phone_number) == 8:
            country, phone_number = phone_number[0], phone_number[1::]
        if len(phone_number) == 10:
            area, phone_number = phone_number[0:3], phone_number[3::]
        return "{0}{1}{2}".format(country, area, phone_number)
    return ""    

def build_file_path(base_path, file_data):
    if file_data[-4::] == ".txt":
        return "{0}/{1}".format(base_path, file_data)
    return ""

def format_numbers(phone_numbers):
    return list(map(lambda phone: "+{0} ({1}) {2}-{3}".format(phone[0], phone[1:4], phone[4:7], phone[7::]), phone_numbers))

def extract_phonenumbers(path="./phones"):
    paths = list(os.walk(path))
    numbers = []
    for path_data in paths:
        if path_data[2] != []:
            files_paths = [build_file_path(path_data[0], file_data) for file_data in path_data[2]]
            for numbers_file_path in list(files_paths):
                if numbers_file_path != "":
                    with open(numbers_file_path) as f:
                        numbers.extend([parse_number(line.rstrip('\n')) for line in f])
    normalized_numbers = list(set(numbers))
    normalized_numbers.sort()

    if normalized_numbers[0] == "":
        normalized_numbers.pop(0)
    
    return format_numbers(normalized_numbers)

if __name__ == "__main__":
    print('Formatted phone numbers:')
    print("\n".join(extract_phonenumbers()))