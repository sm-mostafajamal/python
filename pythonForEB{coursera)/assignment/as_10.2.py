"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

fname = input("Enter file name: ")
fh = open(fname)
count = dict()
for line in fh:
    if not line.startswith("From "):continue
    word = line.split()
    word = (word[5])
    h,s,ms = word.split(":")
    #print (h)
    count[h] = count.get(h, 0) + 1
#print(count)
lst = list()
for k,v in list(count.items()):
	lst.append((k,v))
	lst.sort()
for k,v in lst:
	print(k,v)