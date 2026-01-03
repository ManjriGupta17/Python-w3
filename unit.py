# Original list
fruits = ["apple", "guava", "strawberry", "avocado"]


# 1. append()
fruits.append("banana")
print(fruits)

# 2. insert()
fruits.insert(1, "mango")
print(fruits)

# 3. extend()
fruits.extend(["kiwi", "papaya"])
print(fruits)

# 4. remove()
fruits.remove("guava")
print(fruits)

# 5. pop()
fruits.pop()
print(fruits)

# 6. index()
print("Index of apple:", fruits.index("apple"))

# 7. count()
print("Count of apple:", fruits.count("apple"))

# 8. sort()
fruits.sort()
print("After sort:", fruits)

# 9. reverse()
fruits.reverse()
print("After reverse:", fruits)

# 10. copy()
new_list = fruits.copy()
print("Copied list:", new_list)

# 11. clear()
fruits.clear()
print("After clear:", fruits)

                #  day2
 ### TUPLES
#  THEY ARE IMMUTABLE USE () BRACKET
tup=(2,1,3,1)
print(tup)
print(type(tup))
tup1=()
print(tup1)
print(type(tup1))

tup1= (1,)# isme yeh 1 ko tuple smjhega
print(type(tup1))

tup1=(1) # isme 1 ko integer smjhega
print(type(tup1))

tup1=("hello", )
print(type(tup1))
##single value ke baad 
# ek comma lagana complulsory tbhi wo usko tuple smjhega
tup=(1,2,3,4)
print(tup.count(2))

            #    day3
print(sum(tup))
print(min(tup))
print(max(tup))
print(len(tup))
print(tup.index(2))
print(tup[-4])
tpl=(10,20,30,40,50,60)
m=tpl+(70,)#tuple is add only in tuple 
# if tpl +70 IT WILL GIVE ERROR
print(m)
print(tpl*3)
print(tpl[0])
print(tpl[0:4])
print(tpl[0:5:2])
print(tpl[::-1])#reversing
a=(20,30)
b=(20,30)
print(a==b)
c=("20","30")
print(b==c)
for c in b:
    print(b)
