def create_adder(x):
    def adder(y):
        return x + y
    return adder


add10 = create_adder(10)


v1 = add10(30)

print("v1={}".format(str(v1)))


def inc(i):
    return i + 1


l0 = [1, 2, 3, 4]
l1 = list(map(add10, l0))

print(l0)
print(l1)
