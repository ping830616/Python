largest = None
smallest = None
while True:
    try:
        num = input("Enter a number:")
        if num == 'done':break
        num=int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num
    except:
        print("Invalid input")

print("Maximun is", largest)
print("Minimum is", smallest)
