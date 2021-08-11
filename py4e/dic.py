name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

#list
words = list()

for line in handle:
    if not line.startswith("From:"): continue
    line = line.split()
    words.append(line[1])

#Dictionary
counts = dict()

for word in words:
    counts[word]=counts.get(word,0)+1

#Find the maximum number of counts for the email adress
maxkey = None
maxval = None

for key, val in counts.items():
    if maxval is None or val > maxval:
        maxkey = key
        maxval = val
#The outcome for the maximals
print(maxkey, maxval)
