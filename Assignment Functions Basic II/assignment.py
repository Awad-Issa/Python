def count(n):
    list = []
    for i in range(n, -1, -1):
        list.append(i)
    return list
# print(count(30))

# print(count(9))

def retrn(list):
        print(list[0])
        return list[1]
# print(retrn([3,7]))

def firstplus(list):
    return list[0]+len(list)
# print(firstplus([3,4,3,4,2,6,8]))

def great(list):
    newlist=[]
    count=0
    for i in range(len(list)):
        if list[i] > list[1]:
            count += 1
            newlist.append(list[i])
    print(count)
    return newlist
# print(great([3,4,3,10,6,7,4,2,6,8]))

def lengthh(length,value):
    list=[]
    for i in range(length):
        list.append(value)
    return list
print(lengthh(3,5))
