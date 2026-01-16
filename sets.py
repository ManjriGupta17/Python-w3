# thisset = {"apple", "banana", "cherry"}
# print(thisset)
# print(type(thisset))
# thisset.add("orange")
# thisset={"Apple","banana", True,1,2}
# print(thisset)
# thisset={"apple","banana","cherry",False,1,2}
# print(thisset)
# print(len(thisset))
# set1={"abc",True,False,1,40}
# print(set1)
# print(type(set1))
# thisset =set(("apple", "banana", "cherry"))
# print(thisset)

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# thisset={"Apple","Mango","cherry"}
# for x in thisset:
#     print(x)
# print("Apple" not in thisset)
# thisset.add("Orange")
# print(thisset)
# print(len(thisset))
# thisset={"Apple","Mango","cherry"}
# myList=["Kiwi","Strawberry"]
# c=thisset.update(myList)
# print(thisset)
# thisset.remove("Mango")
# print(thisset)
# thisset.discard("cherry")
# print(thisset)
# x=thisset.remove("Kiwi")
# print(x)
# print(thisset)
# #remove(),discard(),pop()does the same work
# thisset.clear()
# print(thisset)
# thisset={"Apple","Mango","cherry"}
# del thisset
# print(thisset)
# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)
# set3 = set1 | set2
# print(set3)
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"Shivi", "Manjri"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4)
# print(myset)
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
