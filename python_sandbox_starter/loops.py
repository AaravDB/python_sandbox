# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

b=[1,2,3,4]

# While loops execute a set of statements as long as a condition is true.
def listincrementer(a):
    i=0
    while i<len(a):
        a[i]=a[i]+5
        i=i+1
listincrementer(b)
print(b)

