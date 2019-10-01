import csv
import sys

x = open("./data/weather.csv", encoding='utf-8-sig')
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


def partitionEqualWidth(*list):
    for i in range(0, len(list)):
        if list[i] in listAttr:
            attr = list[i]
            listData = []
            n = 5
            for i in range(0, len(dataDict)):
                value = dataDict[i].get(attr)
                if value:
                    listData.append(int(value))
            Min = min(listData)
            Max = max(listData)
            bins = []
            width = (Max-Min) / n
            for i in range(0, n + 1):
                bins = bins + [int(Min + width * i)]
            for i in range(0, len(dataDict)):
                value = float(dataDict[i].get(attr))
                for j in range(0, n):
                    if bins[j] <= value <= bins[j+1]:
                        dataDict[i][attr] = '[' + \
                            str(bins[j])+','+str(bins[j+1])+']'
        else:
            print(f'Attribute {list[i]} is not exist.')


partitionEqualWidth('temperature', 'humidity')
print(dataDict)

try:
    with open("./data/output1.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=listAttr)
        writer.writeheader()
        for i in range(0, len(dataDict)):
            writer.writerow(dataDict[i])
except IOError:
    print("I/O error")
