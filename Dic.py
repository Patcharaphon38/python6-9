car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print (car['brand'])
#show key
print (car.keys())
#เพิ่มค่าในDic
car["color"] = "red"
print (car.keys())
print(car)
#แก้ไขค่าในDic
car["year"] =2018
print(car)
#ลบค่าในDic
car.pop('color')
print(car)
#coppyค่าไปdicอื่น
vel = dict(car)
print('veldic:',vel)
#เก็บlist ในdic
car["part"] = ["body","wheel","light","etc..."]
print('listPart :',car)
#เก็บค่าในdic
#เพิ่มค่าdicแบบ  Nested dic
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
 },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
 },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
 }
}
print(myfamily['child3']['year'])
#พัชรพล พรจันเท้า เลขที่38 6/9