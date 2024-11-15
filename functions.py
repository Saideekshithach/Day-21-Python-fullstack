'''a=10
b=20
print("the sum is ",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is ",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is ",a+b)
print("the difference is",a-b)
print("the product is",a*b)'''

'''def calculate(a,b):
    print("the sum is ",a+b)
    print("the difference is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def division(a,b):
    print("the Integer division is",a//b)
    print("the float division is",a/b)
    print("the power is",a**b)
division(20,10)
division(10,40)
division(2,5)'''


'''def add(a,b):
    c=a+b
    print(c)
add(2,6)'''
'''
while True:
    def cal():
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(a+b)
    cal()
 '''
'''
def data():
    fname=input("fname")
    lname=input("lname")
    print((fname+" "+lname).title())
data()
data()
'''
#print v/s return
'''
def mul(a,b):
    print(a*b)
mul(5,6)
'''
'''
def mul(a,b):
    return a*b
print(mul(4,5))
'''
'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)
'''

def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(3,6))



