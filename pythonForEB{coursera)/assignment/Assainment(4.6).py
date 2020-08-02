def computepay(h,r):
    if h > 40:
        pay = h * r
    return pay


hour = input("Enter Hour:")
h = float(hour)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h,r)
print("Pay",p)
