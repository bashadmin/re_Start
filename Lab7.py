from random import randint as ri
x = ri(0,33)
print(x)
mixedList = [55, 23432, 349.50, False, True, "Hello world", [1,2,3,'a','b'], "hi", 2, x]
for item in mixedList:
    print(f"{item} is of data type {type(item)}")
    print("{} is of the data type {}".format(item, type(item)))
git pull github.com:bashadmin/re_Start.git master
