# phone_numbers_parser

## Task:

    Write an application that finds all phone numbers in a set of text files located in a directory tree starting with <somewhere>. 
    Files should be processed regardless of the nesting level. 
    At the same time, only text files with .txt extension need to be processed, and the others should be ignored.
    
    Phone numbers in the source files can be given with the country code:
    +7 812 number
    +7 (495) number
    +7812number
    +7812 number
    7-812-number
    
    With a three-digit area code:
    (812) number
    812number
    812 number
    095-number

    Or none at all. At the same time the number can have different spellings:
    123-4567
    123-45-67
    1234567
    
    If the city code is not specified, it is considered equal to 812, 
    if the country code is not specified, it is considered equal to 7.
    You need to find all the numbers in all of the files. 
    
    Change formatting to the unified "full" format
    +7 (812) 123-4567
    
    remove duplicates and print the list of numbers in ascending order.

## Asumptions  
1. National numbers always have 7 digits
2. Only numeric phones are valid  
    i.e:   
    +7 (812)-1CALLME isn't valid
    +7 (812)-1234567 is valid
3. Area codes have 3 digits
4. Country code have 1 digit

## Reqs
1. Docker
2. Docker-compose (optional)

## How to use it:
Create or edit a .txt file inside the **"phones"** folder.   
Add one phone per line into the created/edited file.

### Using docker:
Run:  

    docker build --rm -f "Dockerfile" -t phones_formatter:latest "."
    docker run phones_formatter:latest

### Using docker-compose:
Run:  

    docker-compose up

Check the output.