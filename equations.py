def exponent(x):
    result=1
    for n in range(1,120):
        result = result + helper2(x, n)/helper(n)
    return result
def helper(n):
    x=1
    for i in range(int(n)):
        x=x*(i+1)
    return x

def abs1(x):
    if x<0:
        x=x*(-1)
    return x

def helper2(x, n):
    temp =1
    if int(n) == 0:
        return 1
    if int(n) == 1:
        return x
    for i in range(n):
        temp = temp * x
    return temp

def ln(x):
    epsilon = 0.001
    yn=x-1.0
    yn1=yn + 2*((x-exponent(yn))/(x+exponent(yn)))
    while abs1(yn-yn1)>epsilon:
        yn=yn1
        yn1=yn + 2*(x-exponent(yn))/(x+exponent(yn))
    return yn1    

def XtimesY( x , y ):    
    if x>0:      
        lnx = ln(x)
        power=lnx*y
        result= exponent(power)
    else:
        result=0.0
    return result

def sqrt(x,y):
    return (XtimesY(y,1/x))

def calculate(x):
    if(x<=0):
        result=0
    else:
        result= exponent(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x, x)
        result = float('%0.6f' % result)
    return result