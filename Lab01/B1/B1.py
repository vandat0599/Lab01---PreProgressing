import csv
import sys

x = open("./data/credit.csv", encoding='utf-8-sig')
countries = []
data = list(x)
listAttr = data[0].lstrip().rstrip().split(",")
dataDict = []
for i in range(1, len(data)):
    item = {}
    lineList = data[i].lstrip().rstrip().split(",")
    for j in range(0, len(listAttr)):
        item.update({listAttr[j]: lineList[j]})
    dataDict.append(item)

# function return a normalized value


def normalizeValue(min, max, value):
    return (value-min)/(max-min)

# Task a:


def minMaxNormalization(*Attrlist):
    for i in range(0, len(Attrlist)):
        if Attrlist[i] in listAttr:
            attr = Attrlist[i]
            listData = []
            Min = Max = 0
            for i in range(0, len(dataDict)):
                value = dataDict[i].get(attr)
                if value:
                    listData.append(float(value))
            listData.sort()
            Min = listData[0]
            Max = listData[len(listData)-1]
            for i in range(0, len(dataDict)):
                if dataDict[i].get(attr)
                    value = float(dataDict[i].get(attr))
                    normalizedvalue = normalizeValue(Min, Max, value)
                    dataDict[i][attr] = normalizedvalue
        else:
            print(f'Attribute {Attrlist[i]} is not exist.')


minMaxNormalization('duration')


try:
    with open("./data/output.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=listAttr)
        writer.writeheader()
        for i in range(0, len(dataDict)):
            writer.writerow(dataDict[i])
except IOError:
    print("I/O error")
