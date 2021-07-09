from collections import defaultdict

MRO = defaultdict(set)

statements = int(input())

for n in range(statements):
    d = dict(input_().split() for _ in range(n))
    for key, value in input_:
        MRO[key].update(value)


def is_subclass(class_, of_):
    return class_ == of_ or of_ in MRO[class_]
