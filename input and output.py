#to open or read a file
'''f=open("file.txt")
data=f.read()
print(data)
f.close()'''
#to write a file
'''st="i forgot "

f=open("file.txt","w")
f.write(st)
f.close()
'''

#to read as per line together
 
'''f=open("file.txt")
line=f.readlines()
print(line,type(line))
f.close()'''

#read line one by one

'''f=open("file.txt")
line1=f.readline()
print(line1,type(line1))
line2=f.readline()
print(line2,type(line2))
line3=f.readline()
print(line3,type(line3))
line4=f.readline()
print(line4,type(line4))
line5=f.readline()
print(line5,type(line5))

'''

#reading line through loop
'''
f=open("file.txt")

line=f.readline()

while (line!=""):
    print(line)
    line=f.readline()
f.close()'''


#using APPEND function
'''st="new string"
f=open("file.txt","a")

f.write(st)

f.close()
'''

# using with statement

with open("file.txt")as f:
    print(f.read())