# Python has functions for creating, reading, updating, and deleting files.
myFile=open('myfile.txt','w')
print(myFile.name)
print(myFile.closed)
print(myFile.mode)
myFile.write('I love pasta')
myFile.close()

myFile=open('myfile.txt','a')
myFile.write(' and I am a great person')
myFile.close()
myFile=open('myfile.txt','r+')
text=myFile.read(100)
print(text)

