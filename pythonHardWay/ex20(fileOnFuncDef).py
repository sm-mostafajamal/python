from sys import argv

script, input_file = argv


def print_all(files):                                    # replacing files with current_file variable
    print(files.read())

def rewind(files):
    files.seek(0)

def print_a_line(line_count, files):
    print(line_count, files.readline(), end = '')         # Counting the line and printing line by line

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)                     # Printing the files and Replacing files with current_file variable

print("Now let's rewind, kind of like a tape.")
rewind(current_file)                        # Rewinding the line starting from line one and replacing files variable

print("Let's print three lines: ")

# Countig lines and printing lines
current_line = 1
print_a_line(current_line, current_file)    # replacing line_count to current_line

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1             # counting the line
print_a_line(current_line,current_file)     # printinf the line number and the line
