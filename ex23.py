import sys

script, encoding, error = sys.argv

#Here we are taking a main function with some arguments
def main(language_file, encoding, errors):
    #The first line is specifing a line taking some input from the language file
    line = language_file.readline()
# If the line exists we are printing the line then we are calling the function again
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

#Now we are going to define the print_line function

def print_line(line, encoding, errors):
    next_lang = line.strip()

    raw_bytes = next_lang.encode(encoding, errors=errors)

    cooked_string = next_lang.decode(encoding, errors = errors)

    print(raw_bytes, "<====>", cooked_string)
    languages = open("languages.txt", encoding = "utf-8")

    main(languages, encoding, error)
    



