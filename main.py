statements = int(input())

for n in range(statements):
    inpt = input().replace(":", "").split()
    subclass = inpt.pop(0)
    parents = []
    for i in inpt:
        existing_parents = globals()[i].__bases__
        globals()[i] = type(i, existing_parents, {})
        parents.append(globals()[i])
    p = tuple(parents)
    globals()[subclass] = type(subclass, p, {})

queries = int(input())

for i in range(queries):
    qr = input().split()
    if issubclass(globals()[qr[1]], globals()[qr[0]]):
        print('Yes')
    else:
        print('No')
