import re
fname = input("File Name: ")
file = open(fname)

total = 0
for line in file:
    line = line.rstrip()
    x = re.findall("[0-9]+", line)
    for i in x:
        total = total + int(i)
print(total)
