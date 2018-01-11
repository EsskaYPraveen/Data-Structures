def sum(c):
    sum=0
    for i in c:
        sum=sum+i

    return sum
a=[1,2,3,4,5,6,7]
b=sum(a)
print b

def summ(c):
    if len(c)==1:
        return c[0]
    else:
        return c[0]+summ(c[1:])

print(summ([1,2,3,4,5,5,5]))

def hex(a,base):
    str="0123456789ABC"
    if a<base:
        return str[a]
    else:
        return hex(a//base,base)+str[a%base]

print(hex(465456,16))

s="MalayalaM"
def palend(str):
    if len(str)<1:
        return True
    if str[0]==str[len(str)-1]:
        return palend(str[1:len(str)-1])
    else:
        return False


if palend(s):
    print("is Palendrome")
else:
    print("NOt Palendrome")



