import csv
import sys
import operator

x = open("./data/credit.csv", encoding='utf-8-sig')
data = list(x)
listAttr = data[0].lstrip().rstrip().split(",")
dataDict = []
for i in range(1, len(data)):
    item = {}
    lineList = data[i].lstrip().rstrip().split(",")
    for j in range(0, len(listAttr)):
        item.update({listAttr[j]: lineList[j]})
    dataDict.append(item)

# print(dataDict)
# e f


def getMeanOfAttr(attr):
    result = 0
    if attr not in listAttr:
        print("'", attr, "': not found")
    else:
        for item in dataDict:
            if item.get(attr) == '':
                result += 0
            else:
                if isinstance(item.get(attr), str):
                    result += int(item.get(attr), 10)
                else:
                    result += item.get(attr)
    return int(result/len(dataDict))


def getHighestFreqValue(attr):
    freq = {}
    if attr not in listAttr:
        print("'", attr, "': not found")
        return ''
    else:
        for item in dataDict:
            if item.get(attr) not in freq:
                freq.update({item.get(attr): 1})
            else:
                freq[item.get(attr)] = freq.get(item.get(attr)) + 1
    # print(freq)
    return max(freq.items(), key=operator.itemgetter(1))[0]


def isNumeric(attr):
    i = 0
    if attr not in listAttr:
        print("'", attr, "': not found")
        return False
    else:
        for item in dataDict:
            i += 1
            if item.get(attr) != '' and isinstance(item.get(attr), str) and not(item.get(attr).isnumeric()):
                return False
    return True

# e


def removeMissingInstance(attrList):
    removeItemCount = 0
    # check exist attr
    for attr in attrList:
        if attr not in listAttr:
            print("'", attr, "': not found")
    for item in dataDict:
        for attr in attrList:
            if item.get(attr) == '':
                dataDict.remove(item)
                removeItemCount += 1
    print("removed:", removeItemCount, "items")

# f


def insertMissingInstance(attrList):
    removeItemCount = 0
    # check exist attr
    for attr in attrList:
        if attr not in listAttr:
            print("'", attr, "': not found")
    for item in dataDict:
        for attr in attrList:
            if item.get(attr) == '':
                if isNumeric(attr):
                    item[attr] = getMeanOfAttr(attr)
                else:
                    item[attr] = getHighestFreqValue(attr)
                removeItemCount += 1
    print("effect:", removeItemCount, "items")


# isNumeric("duration")
# removeMissingInstance(["asdf"])
# print(getMeanOfAttr("duration"))
# getHighestFreqValue("class")
insertMissingInstance(["duration", "class"])


try:
    with open("./data/output.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=listAttr)
        writer.writeheader()
        for i in range(0, len(dataDict)):
            writer.writerow(dataDict[i])
except IOError:
    print("I/O error")

print("Done!!!")
