def isLeapyear(year):
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return True
    else:
        return False

for i in range(2000,3001):
    if(isLeapyear(i)):
        print(i,end=' ')