import csv
import sys
import math 
# Function for B
def mean(dictionary, properties):
	mean = 0
	for i in range(len(dictionary)):
		if dictionary[i][properties] != '':
			mean += int(dictionary[i][properties])
	return mean/(len(dictionary))

def standardDeviation(data,properties):
	m = mean(data,properties)
	s = 0 
	for i in range(len(data)):
		if data[i][properties] != '':
			s+= (int(data[i][properties]) - m)**2
	return math.sqrt(s/(len(data)-1))

def absoluteDeviation(data, properties):
	m = mean(data,properties)
	s = 0
	for i in range(len(data)):
		s+=abs(int(data[i][properties]) - m)
	return s/len(data) 


def zScore(data, properties):
	m = mean(data,properties)
	# absDev = absoluteDeviation(data,properties)
	stanDev =standardDeviation(data,properties)
	for i in range(len(data)):
		if data[i][properties] != '':
			data[i][properties] = str((int(data[i][properties]) - m)/stanDev)	

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
				residual -=1
			else:
				numMemBin.append(num - 1)
	return numMemBin

def createBin(data,properties,numbin):
	listdata = []
	for i in range(len(data)):
		if data[i][properties] != '':
			listdata.append(int(data[i][properties]))
	listdata.sort()
	numMemBin = createNumMemBin(listdata,numbin)
	local = len(listdata)-1
	element = int(listdata[local]) + 1
	listdata.append(element)
	binning = []
	count = 0
	for i in numMemBin:
		a =count
		b = count + i
		binning.append([listdata[a],listdata[b]])
		count +=i
	a = numbin-1
	b = len(listdata)-2
	binning[a][1] = listdata[b]
	return binning

def EqualDepthPartitioning(data, properties, numbin):
	binning = createBin(data, properties, numbin)
	for i in range(len(data)):
		if data[i][properties]:
			for j in range(len(binning)):
				a = data[i][properties]
				if j < (len(binning)-1):
					if int(a) >= binning[j][0] and int(a) < binning[j][1]:
						data[i][properties] = "["+ str(binning[j][0]) + "," + str(binning[j][1]) + ")"
						break
				elif j == (len(binning) -1):
					if int(a) >= binning[j][0] and int(a) <= binning[j][1]:
						data[i][properties] = "["+ str(binning[j][0]) + "," + str(binning[j][1]) + "]"
						break
	print(data)


# this is a new commnent
# RUN

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


# zScore(dataDict,"mot")

# print(dataDict)


EqualDepthPartitioning(dataDict,"temperature",10)


