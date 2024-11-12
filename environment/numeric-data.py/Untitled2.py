print("Pyhton has three numeric types: int, float, and complex")


myValue=1

print(myValue)

print(type(myValue))

print(str(myValue) + "is of the data type" + str(type(myValue)))
myValue=3.14
print(myValue)
print(type(myValue))

print(str(myValue) + " is of the data type" + str(type(myValue)))

myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type" + str(type(myValue)))

myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myMixedTypeList= [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
