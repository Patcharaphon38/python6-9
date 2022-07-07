fruitsTuple = ("apple","banana", "cherry","kiwi")
fruitslist = ["apple","banana", "cherry","kiwi"]
print(fruitsTuple[1:])
print(fruitslist[0])
#เปลี่ยนค่าtuple
fruitslist[1] = "mango" #เปลี่ยนในlist
print(fruitslist)
#tupleไม่สามารถเปลี่ยนค่าโดยตรงได้ ต้องแปลงเป็นlistก่อน
x = list(fruitsTuple)
x[1] = "mango"
fruitsTuple = tuple(x)
print(fruitsTuple)
#เพิ่มค่าในTuple  
x = list(fruitsTuple)
x.append("orange")
fruitsTuple = tuple(x)
print(fruitsTuple)
#ลบค่าในtuple
x = list(fruitsTuple)
x.remove("kiwi")
fruitsTuple = tuple(x)
print(fruitsTuple)
x = range(3, 20)
for n in x:
    print(n)
    x = range(3, 20, 2)
for n in x:
    print("step3:",n)
