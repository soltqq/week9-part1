def value(item):
    return item[1]

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
top3= dict(sorted(my_dict.items(), key=value, reverse=True)[:3])
print(top3)