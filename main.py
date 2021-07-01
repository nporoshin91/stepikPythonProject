from collections import defaultdict

MRO = defaultdict(set)

# TODO: defaultdict
# set - possible operations

for key, descendants in ...:
    MRO[key].update(descendants)


def is_subclass(class_, of_):
    return class_ == of_ or of_ in MRO[class_]
