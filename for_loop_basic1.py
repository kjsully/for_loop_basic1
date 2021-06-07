for x in range(151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1, 101):
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print ("Coding Dojo")
    else:
        print(x)

oddcount = 0
for x in range(0, 500001):
    if x % 2 != 0:
        oddcount = oddcount + x
print(oddcount)

i = 2018
while i >= 0:
    if i % 2 == 0:
        print(i)
    i -= 4

lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)
    
