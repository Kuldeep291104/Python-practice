#strings are immutable
'''name="kuldeep"
name_short=name[-4:-1]
print(name_short)
character1=name[1]
print(character1)'''
#slicing with skip value

'''a=("01234567890")
print(a[1:5:2])
'''
#functions of strings
'''name=("kuldeep rathod")
print(len(name))
print(name.endswith("ep"))
print(name.startswith("n"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(name.replace("k","r"))
'''
#q=("i am a good guy \n my name is kuldeeo") break a line

'''name=input("enter your name")
print(f"good afternoon{name}" )
'''




#letter='''Dear <|Name|>,You are selected!<|Date|>'''
#print(letter.replace("<|Name|>","Kuldeep").replace("<|Date|>","29 November 2004"))

#problem4
'''detect=("hi my name  is kuldeep")
print(detect.find("  "))
print(detect.replace("  "," "))'''

#problem 5

Letter="Dear Harry,\n\t this python course is nice.\nThanks!"
print(Letter)