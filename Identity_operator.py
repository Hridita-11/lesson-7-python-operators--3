x = 6
if (type (x) is int):
    print("true")

else:
    print("false")

x = 9.7 
if(type(x) is not float):
    print("true")
else:
    print("false")

x = 50 
y = 50 
if (x is y):
    print("x & y same identity")

y = 30 
if (x is not y):
    print(" x and y has different identity")
