# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def sayhello(name):
    print(f"hello {name}")

sayhello('Aarav')

def getdiff(num1,num2):
    total=num1-num2
    return total

print(getdiff(3,4))


def listincrementer(a):
    for i in range(len(a)):
        a[i]=a[i]+5

b=[1,2,3,4,5]
listincrementer(b)
print(b)
