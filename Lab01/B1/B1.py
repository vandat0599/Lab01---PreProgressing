import csv
import sys
# this is a new commnent
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

print(dataDict)
