# numlist = list()
# while True:
#     inp = input('Enter a number:')
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)
#
# average = sum(numlist)/len(numlist)
# print('The average value',average)

list = '123;234;345'
x=list.split(';')
print(x)

for i in x:
    print(i)
