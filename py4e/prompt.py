# Use words.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fname:
#     fname = fname.rstrip()
# fr = fh.read()
# print(fr.upper())

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        value = float(line[line.find(":")+1:])
        total += value
answer = total / count
print("Average spam confidence:", answer)
