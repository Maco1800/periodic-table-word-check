"""
todo
add option for checking similar sound
"""
import periodictable
elements = [element.symbol for element in periodictable.elements]
del elements[0]#for some reason neutron is added in the module idk so just remove it
s=input('enter : ')
s2=''
i=0
while i < len(s):
    if s[i].upper()+s[i+1:i+2].lower() in elements and len(s)>i+1:
        s2=s2+s[i].upper()+s[i+1:i+2].lower()
        i+=1
    elif s[i].upper() in elements:
        s2=s2+s[i].upper()
    i+=1

if s.lower()==s2.lower():
    print(s2)
else:
    print('nope')




    