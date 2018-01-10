def sum(c):
    sum=0
    for i in c:
        sum=sum+i
    return sum




a=[1,2,3,4,5,5]
b=sum(a)
print(b)

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
       return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

def toStr(n,base):
    convertString="0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]


print(toStr(1453,16))


def palendrome(str):
    a=len(str)

    if a<=1:
        return str[a]
    else:
        print(palendrome(str[:a]))
        return str[a] + palendrome(str[:a])

b="MAdam"
c=palendrome(b)
if b == c:
    print("It is a Palendrome")
else:
    print("It is not a Palendrome")






