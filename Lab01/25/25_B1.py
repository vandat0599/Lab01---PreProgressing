import csv
import sys
import operator
import math

# valid command: preprocess --input {inputFilePath(*.csv)} --output {outputFilePath(*.csv)} --task {taskName} --propList {setOfAttr}
argvList = sys.argv
print(argvList)
if "preprocess" in argvList and "--input" in argvList and "--output" in argvList and "--task" in argvList and "--propList" in argvList:
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
                    if dataDict[i].get(attr):
                        value = float(dataDict[i].get(attr))
                        normalizedvalue = normalizeValue(Min, Max, value)
                        dataDict[i][attr] = normalizedvalue
            else:
                print(f'Attribute {attrList[i]} is not exist.')

    def partitionEqualWidth(n, attrList):
        for i in range(0, len(attrList)):
            if attrList[i] in listAttr:
                attr = attrList[i]
                listData = []
                for i in range(0, len(dataDict)):
                    value = dataDict[i].get(attr)
                    if value:
                        listData.append(int(value))
                Min = min(listData)
                Max = max(listData)
                bins = []
                width = math.ceil((Max-Min) / n)
                for i in range(0, n + 1):
                    bins = bins + [int((Min + width * i))]
                print(bins)
                for i in range(0, len(dataDict)):
                    if dataDict[i].get(attr):
                        value = float(dataDict[i].get(attr))
                        for j in range(0, n):
                            if bins[j] <= value <= bins[j+1]:
                                dataDict[i][attr] = '[' + \
                                    str(bins[j])+','+str(bins[j+1])+']'
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

    # Function for B
    def mean(dictionary, properties):
        mean = 0
        for i in range(len(dictionary)):
            if dictionary[i][properties] != '':
                mean += int(dictionary[i][properties])
        return mean/(len(dictionary))

    def standardDeviation(data, properties):
        m = mean(data, properties)
        s = 0
        for i in range(len(data)):
            if data[i][properties] != '':
                s += (int(data[i][properties]) - m)**2
        return math.sqrt(s/(len(data)-1))

    def absoluteDeviation(data, properties):
        m = mean(data, properties)
        s = 0
        for i in range(len(data)):
            s += abs(int(data[i][properties]) - m)
        return s/len(data)

    def zScore1(data, properties):
        for attr in properties:
            if attr in listAttr:
                m = mean(data, attr)
                # absDev = absoluteDeviation(data,properties)
                stanDev = standardDeviation(data, attr)
                for i in range(len(data)):
                    if data[i][attr] != '':
                        data[i][attr] = str(
                            (int(data[i][attr]) - m)/stanDev)
            else:
                print("'{}' not found".format(attr))

    # function for D
    def createNumMemBin(listdata, numBin):
        num = math.ceil(len(listdata)/numBin)
        residual = len(listdata) - int(len(listdata)/numBin)*numBin
        numMemBin = []
        if residual == 0:
            for i in range(numBin):
                numMemBin.append(num)
        else:
            for i in range(numBin):
                if residual > 0:
                    numMemBin.append(num)
                    residual -= 1
                else:
                    numMemBin.append(num - 1)
        return numMemBin

    def createBin(data, properties, numbin):
        listdata = []
        for i in range(len(data)):
            if data[i][properties] != '':
                listdata.append(int(data[i][properties]))
        listdata.sort()
        numMemBin = createNumMemBin(listdata, numbin)
        local = len(listdata)-1
        element = int(listdata[local]) + 1
        listdata.append(element)
        binning = []
        count = 0
        for i in numMemBin:
            a = count
            b = count + i
            binning.append([listdata[a], listdata[b]])
            count += i
        a = numbin-1
        b = len(listdata)-2
        binning[a][1] = listdata[b]
        return binning

    def EqualDepthPartitioning1(data, properties, numbin):
        for attr in properties:
            if attr in listAttr:
                binning = createBin(data, attr, numbin)
                for i in range(len(data)):
                    if data[i][attr]:
                        for j in range(len(binning)):
                            a = data[i][attr]
                            if j < (len(binning)-1):
                                if int(a) >= binning[j][0] and int(a) < binning[j][1]:
                                    data[i][attr] = "[" + \
                                        str(binning[j][0]) + "," + \
                                        str(binning[j][1]) + ")"
                                    break
                            elif j == (len(binning) - 1):
                                if int(a) >= binning[j][0] and int(a) <= binning[j][1]:
                                    data[i][attr] = "[" + \
                                        str(binning[j][0]) + "," + \
                                        str(binning[j][1]) + "]"
                                    break
            else:
                print("'{}' not found".format(attr))

    def zScore(attr):
        zScore1(dataDict, attr)

    def EqualDepthPartitioning(numbin, properties):
        EqualDepthPartitioning1(dataDict, properties, numbin)

    switcher = {
        "removeMissingInstance": removeMissingInstance,
        "insertMissingInstance": insertMissingInstance,
        "minMax": minMaxNormalization,
        "zScore": zScore,
        "partitionEqualWidth": partitionEqualWidth,
        "partitionEqualDepth": EqualDepthPartitioning
    }
    task = argvList[7]
    executeFunc = switcher.get(task)
    if executeFunc is None:
        print(task, "-> Not found")
    else:
        if task == "partitionEqualWidth" or task == "partitionEqualDepth":
            le = argvList[11:len(argvList)]  # songjongki
            if len(le) == 1:
                le[0] = le[0].rstrip("}").lstrip("{")
            executeFunc(int(argvList[9]), list(le))
        else:
            le = argvList[9:len(argvList)]  # songjongki
            if len(le) == 1:
                le[0] = le[0].rstrip("}").lstrip("{")
            executeFunc(list(le))

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
        ---Valid command: preprocess --input {inputFilePath} --output {outputFilePath} --task {taskName} {*} --propList {setOfAttr}
        -----inputFilePath: *.csv
        -----outputFilePath: *.csv")
        -----{*}(optional): support partitionEqualWidth and partitionEqualDepth: require "--bin {number}"
        -----taskName:
        --------a: minMax
        --------b: zScore
        --------c: partitionEqualWidth
        --------d: partitionEqualDepth
        --------e: removeMissingInstance
        --------f: insertMissingInstance
        -----setOfAttr: ex: {id, name, age}""")
