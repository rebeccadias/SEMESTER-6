import numpy as np
import matplotlib.pyplot as plt
def predict(b0,b1,x):
    return b1+b0*x
def coefficient(x,y):
    xm=np.mean(x)
    ym=np.mean(y)
    X2=[(x[i])* (x[i]) for i in range(len(x))]
    Y2=[(y[i])* (y[i]) for i in range(len(y))]
    XY=[(y[i])* (x[i]) for i in range(len(y))]
    num1=sum(y)*sum(X2)-sum(x)*sum(XY)
    den=len(x)*sum(X2)-sum(x)**2
    num2=len(x)*sum(XY)-sum(x)*sum(y)
    b1=num1/den
    b0=num2/den
    return b0,b1

x=list(map(int,input("Enter x (Year of Experience) : ").split()))
y=list(map(int,input("Enter y (Salary in $100): ").split()))

b0,b1=coefficient(x,y)
print("b0 : ",b0,"\n","b1 : ",b1)
n=int(input("Enter value : "))
print("Expected salary : ",predict(b0,b1,n))
x1=np.linspace(min(x),max(x),10)
y1=b1+b0*x1
plt.scatter(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x1,y1,'-r')
plt.show()


# 3 8 9 13 3 6 11 21 1 16 --
# 30 57 64 72 36 43 59 90 20 83 --
# 15