# class Myclass:
#     x = 5

# p1 = Myclass()
# print(p1.x)

# p1= Myclass()
# print(p1.x)
# p2= Myclass()
# print(p2.x)
# p3= Myclass()
# print(p3.x)

# class person:
#     pass 

# class Person:
#     def __init__(self):
#         pass

#Python __init__() Method
# class Person:
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age 

# p1 = Person("Manjri",16)

# print(p1.name)
# print(p1.age)

#Using __init__() makes it easier to create objects with initial values:

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

