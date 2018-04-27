from typing import List

li: List[int] = [10, 1, 2, 3, -1000000.000002]
li.sort()
li.reverse()
print(li)

x = 0
y = 0
for x in li:
    y = "value={:.4f}".format(x)
    print(y)

print("x={}".format(x))
print("y={}".format(y))

se = {1, 2, 3}
se.add(3)
se.add(4)
print(se)

li2 = list(se)
li2.sort(reverse=True)

print(se)
print(li2)


def inc(_x: int):
    return _x + 1


def double(_x):
    return _x * 2


def greater10(_i: int):
    return _i > 10


li = (-1, -2, -3, 4, 10)

dd = [inc(x) for x in li if x > 0]
print("dd = {}".format(dd))

dd1 = (inc(x) for x in dd)
print("dd1 = {}".format(list(dd1)))

dd2 = [x for x in dd if greater10(x)]
print("dd2 = {}".format(list(dd2)))

l2 = [0, 1, 2, 3, 4, 5, 6]

l3 = l2[:3]
print("{} --[:3]--> {}".format(l2, l3))

l3 = l2[0:3]
print("{} --[0:3]--> {}".format(l2, l3))

l3 = l2[0:]
print("{} --[0:]--> {}".format(l2, l3))

l3 = l2[:]
print("{} --[:]--> {}".format(l2, l3))

l3 = l2[0:3:-1]
print("{} --[0:3:-1]--> {}".format(l2, l3))

l3 = l2[3:0:-1]
print("{} --[3:0:-1]--> {}".format(l2, l3))

l5 = range(0, 30)
print("range(0, 30):".format(l5))

l6 = l5[0:10]
print("l5[0:10] -> {}".format(list(l6)))

a = "python"
b = a[2:-20]
print("{} -> {}".format(a, b))

dict1 = {1: "hallo", 2: "klomm"}

dict1[3] = "jj"
dict1[1] = "kk"

for x in dict1.keys():
    print("A elem = {}".format(dict1[x]))

for x in dict1.values():
    print("B elem = {}".format(x))
