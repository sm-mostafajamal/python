"""

9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

fname = input("Enter file name: ")
fh = open(fname)
count = dict()
for line in fh:
    if not line.startswith("From "):continue
    word = line.split()
    word = (word[1])
    #print (word)
    count[word] = count.get(word, 0) + 1
#print(count)

bigW = None
bigC = None

for k,v in count.items():
	if bigC is None or bigC < v:
		bigW = k
		bigC = v
print(bigW, bigC)
    	