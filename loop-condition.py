for index in range(1,11,1) :
    print(index)
    
#loop กับ list
List1 = ['wisanu','Jojo','Jotaro']
for element in List1:
    print(element)
    
#loop กับ dic
Dic = {'name':'Joseph','age':50,'job':'mage'}
for key,Value in Dic.items():
    print(key,':',Value)
List2=[{'name':'Joseph','age':50,'job':'mage'},
       {'name':'wisanu','age':18,'job':'popstar'},
       {'name':'Soranun','age':25,'job':'teacher'},
       {'name':'Tuu','age':70,'job':'soldier'}]
for element in List2:
    for key,Value in element.items():
        print(key,Value)
i = 1
while i<10:
    print(i)
    i+=1
name = input("ชื่อ:")
print(name)   
    
    
    
    