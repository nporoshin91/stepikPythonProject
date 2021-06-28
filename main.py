classes = {}    # {'A': 'E', 'B': {'A, D'}, 'C': {'A'}, 'D': {'C', 'B'}}
statements = int(input())
queries = int(input())


def setup():
    i = input().replace(":", "").split()
    child = i.pop(0)
    classes[child] = set(i)


def finder():
    i = input().split()         # ['E', 'B']
    parent = i[0]
    child = i[1]
    if parent in classes.get(child):
        print('Yes')
    elif parent not in classes.get(child):
        i = [i[1], list(classes[child])]

    elif parent == child:
        print('Yes')
    else:
        print('No')


for n in range(statements):
    setup()
for q in range(queries):
    finder()
