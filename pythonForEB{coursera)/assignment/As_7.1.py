"""
7.1: Write a program to read through a file and print the contents of the file (line by line) all in upper case.
"""
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
File = fh.read()
File = File.rstrip()
print(File.upper())