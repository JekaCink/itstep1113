class Student:
     #print("Привіт, створення класу")
     def __init__(self,name="Женя",group="1113",age=14): #self - посилатися на себе на клас
       self.name=name
       self.group=group
       self.age=age
st1=Student()#об'єкт
# print(st1.name,st1.group,st1.age)
st2=Student(name="Леха",group="1113",age=15)
# print(st2.name,st2.group,st2.age
print(st1)
print(st2)