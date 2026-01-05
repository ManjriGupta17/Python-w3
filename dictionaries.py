# thisdict = {
#     "Name":"Manjri",
#     "Age":"16",
# }
# print(thisdict)
# print(thisdict["Age"])
# print(len(thisdict))
# x=thisdict.get("Name")
# print(x)
# x=thisdict.values()

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
keys= ['one','two','three']
values=[1,2,3]
print("given two lists are :",keys,values)

employee={"Name":"Manjri", "Salary":"1,00,000","age":20}
employee['Dept']='Sales'
print(employee)

employee={"Name":"Manjri", "Salary":"1,00,000","age":20}
myList=employee.items()
for x in myList:
    print(x)

empl={'age':25,"name":"manjri","sirname":"Gupta"}
seq=empl.items()
for key,value in seq:
    print(value,key)

empl.keys()
print(empl)