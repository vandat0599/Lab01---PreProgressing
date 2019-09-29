from CountryOb import *

x = open("countries.txt")
countries = []
data = list(x)
it = iter(data)
line = next(it)
try:
    while True:
        countryOb = CountryOb()
        attr = line[0:line.index("=")]

        countryOb.attr = line[line.index("=") + 1: len(line)]
        # print(countryOb.attr)
        line = next(it)
        while "country" not in line:
            attr = line[0:line.index("=")]
            countryOb.attr = line[line.index("=") + 1: len(line)]
            line = next(it)
        countries.append(countryOb)
except:
    print("Out it")

print(countries[0].attr)
# it = iter(x)
# while():
#     print(next(it))
# for i in x:
#     countryOb = CountryOb()
#     attr = i[0:i.index("=")]
#     countryOb.attr = i[i.index("=") + 1: len(i)]
#     if "country" in i:

# x = CountryOb()
# x.a = 10
# print(hasattr(x, "a"))
