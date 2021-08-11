hrs=input("Enter hours:")
rate=input("Enter rate:")
try:
    h=float(hrs)
    r=float(rate)
except:
    print("Error, please enter numeric input")
    quit()
    
print(h,r)
if h<=40:
    print(h*r)
else:
    print(40*r+(h-40)*(1.5*r))
