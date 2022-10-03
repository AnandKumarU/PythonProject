#simple intrest
#for given principal amount, time and
# rate of interest
def simple_interest(p,t,r):
    print('the principal amount is',p)
    print('the time period is',t)
    print('the rate of interest is',r)

    Si = (p * t * r) / 100
    print('the simple interest is', Si)
    return Si
simple_interest(8,6,8)