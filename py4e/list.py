# The file name is romeo.txt
fname = input("Enter file name: ")
fh = open(fname)

lst = list()
for line in fh:
    words = line.rstrip().split()
    for i in words:
        if i not in lst:
            lst.append(i)
            lst.sort()
print(lst)
