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

