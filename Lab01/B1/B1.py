import csv
import sys
import operator

# valid command: preprocess --input {inputFilePath(*.csv)} --output {outputFilePath(*.csv)} --task {taskName} --propList {setOfAttr}
argvList = sys.argv
print(argvList)
if len(argvList) > 8 and argvList[1] == "preprocess" and argvList[2] == "--input" and ".csv" in argvList[3] and "--output" in argvList[4] and ".csv" in argvList[5] and argvList[6] == "--task" and argvList[8] == "--propList":
    x = open(argvList[3], encoding='utf-8-sig')
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

# a

# function return a normalized value

    def normalizeValue(min, max, value):
        return (value-min)/(max-min)

    # Task a:

    def minMaxNormalization(attrList):
        for i in range(0, len(attrList)):
            print(attrList)
            # print(list[i])
            if attrList[i] in listAttr:
                attr = attrList[i]
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
                    value = float(dataDict[i].get(attr))
                    normalizedvalue = normalizeValue(Min, Max, value)
                    dataDict[i][attr] = normalizedvalue
            else:
                print(f'Attribute {attrList[i]} is not exist.')

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
        print(attrList)
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

    switcher = {
        "removeMissingInstance": removeMissingInstance,
        "insertMissingInstance": insertMissingInstance,
        "minMax": minMaxNormalization
    }
    task = argvList[7]
    executeFunc = switcher.get(task)
    if executeFunc is None:
        print(task, "-> Not found")
    else:
        executeFunc(list(argvList[9:len(argvList)]))
    try:
        with open(argvList[5], 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=listAttr)
            writer.writeheader()
            for i in range(0, len(dataDict)):
                writer.writerow(dataDict[i])
    except IOError:
        print("I/O error")


else:
    print(
        """---Command not found
        ---Valid command: preprocess --input {inputFilePath} --output {outputFilePath} --task {taskName} --propList {setOfAttr}
        -----inputFilePath: *.csv
        -----outputFilePath: *.csv")
        -----taskName:
        --------a: minMax
        --------b: zScore
        --------c: equalWidth
        --------d: .....
        --------e: removeMissingInstance
        --------f: insertMissingInstance
        -----setOfAttr: ex: {id, name, age}""")
