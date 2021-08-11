fname = {'hi hi hello hi hello hey hey hi hello'}

di = dict()
for line in fname:
    line = line.rstrip()
    wds = line.split()
    #print the splited words
    print(wds)
    for word in wds:
        #idiom: retrieve/create/update counter
        di[word] = di.get(word,0)+1
print(di)
