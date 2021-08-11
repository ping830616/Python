
hrs=input("Enter hours:")
rate=input("Enter rate:")
h=float(hrs)
r=float(rate)
if h<=40:
    print("Pay",h*r)
else:
    def computepay(h,r):
        return 40*r+(h-40)*1.5*r
    p = computepay(h,r)
    print("Pay",p)
