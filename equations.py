#205655343, Yafit Ratzon
#Matala number 1

def absolut_func(x:float) -> float:
    if(x<0):
        x*=(-1)  
    return x

#exponent function
def exponent(x:float) -> float:

    i= 0
    e_x_kodem=0.0
    e_x= 1.0
    mone=1
    mechane=1
    while e_x != e_x_kodem :
        mone=mone*x
        mechane=mechane*(i+1)
        e_x_kodem=e_x
        e_x+=mone/mechane
        i+=1
        
    return(e_x)


#ln function
def Ln(x:float) -> float:
    if x <= 0.0: 
        return 0.0
    else:
        yn=x-1.0
        yn_plus_one=yn+2*((x-exponent(yn))/(x+exponent(yn)))
        while absolut_func(yn_plus_one - yn) > 0.001:
            yn=yn_plus_one
            yn_plus_one=yn+2*((x-exponent(yn))/(x+exponent(yn)))
            
        resault=yn_plus_one
        return(resault)


#pow function
def XtimesY(x:float, y:float) -> float:
    if x <= 0.0: 
        return 0.0
    else:
        resault=exponent(y*Ln(x))
        return(resault)


#sqrt function
def sqrt(x:float, y:float) -> float:
    if y <= 0.0 or x==0.0 :
        return 0.0
    resault=XtimesY(y,1/x)
    return(resault)


#calculate function
def calculate(x:float) -> float:
    resault=float('%0.6f' % (exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)))
    return(resault)