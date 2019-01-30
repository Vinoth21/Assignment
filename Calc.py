#Simple Calculator
import math 

def addition(lst):
    return sum(lst)

def substraction(x,y):
    return x-sum(y)

def multiplication(lst):
    m=1
    for x in lst:
       m=m*x
    return m

def division(x):
    r=x[0]
    for i in x[1:]:
        r=float(r)/i
    return r
    #return float(x)/y

def power(x,y):
    r=1
    for i in range(y):
       r=r*x
    return r
       
def logarithamic(x):
    return math.log(x,10)
num=1
while num>0:
	print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exponential\n6.Logarithamic")
	num=int(input("Enter the Choice of operation or '-1' to Quit : "))
	print ("\n")	
	if num==1:
    		l=a = [int(x) for x in input("Enter a list of numbers to be added : ").split()]
    		print ("Sum of numbers is %d" %addition(l))
	elif num==2:
    		l=[int(x) for x in input("Enter two numbers to be subtracted : ").split()]
    		print ("Substracted result is %d" %substraction(l[0],l[1:]))
	elif num==3:
    		l=[int(x) for x in input("Enter a list of numbers to be multiplied : ").split()]
    		print ("Product of the given numbers is %d " %multiplication(l))
	elif num==4:
    		l=[int(x) for x in input("Enter numbers to perform division : ").split()]
    		print ("The result of division of given numbers is %d" %(division(l)))
	elif num==5:
    		l=[int(x) for x in input("Enter two numbers to perform exponential operation : ").split()]
    		print ("The %d power of %d is %d" %(l[1],l[0],power(l[0],l[1])))
	elif num==6:
    		l=int(input("Enter number to find its log value : "))
    		print ("The Logarithamic value of %d is %d " %(l,logarithamic(l)))
	else:
    		print ("Thank You")
else:
	print ("Unexpected input")
