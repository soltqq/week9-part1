import operator

def value(item):
    return item[1]

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

ascending = dict(sorted(d.items(), key=value))

descending = dict(sorted(d.items(), key=value, reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)
