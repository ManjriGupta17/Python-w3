# i=1
# while i<5 :
#     j = 1 
#     while j < 5:
#         print(j)
#     i=i+1
# i = 1
# while i <=5:
#     j=1
#     while j<=i:
#         print('*',end="")
#     print()
#     i=i+1
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
       