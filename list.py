Fruits = ['apple',"banana","cherry","orange"]
#เปลี่ยนค่าในlist
Fruits[1] = "blackcurrant"
print(Fruits)
Fruits[1:3] = ["kiwi", "watermelon","melon"]
print(Fruits)
#เพิ่มค่าในlist
Fruits.append("mango")
print(Fruits)
Fruits.insert(2,"durian")
print(Fruits)
tropical = ["papaya","pineapple"]
Fruits.extend(tropical)
print(Fruits)
#ลบค่าในlist
Fruits.remove("durian")
print(Fruits)
Fruits.pop(3)
print(Fruits)
#del Fruits ลบทุกอย่าง
#เรียงค่าในlist
Fruits.sort()
print(Fruits)
Fruits.sort(reverse=True)
print(Fruits)
#นายพัชรพล พรจันเท้า 38 6/9