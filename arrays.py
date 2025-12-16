cars = ["Gwagnar","Defender","Alto"]
print(cars[0])
cars[0]= "Toyoto"
print(cars)
x=len(cars)

for x in cars:
    print(x)

cars.append("Honda")

cars.pop(1)
cars.remove("Honda")
print( cars)