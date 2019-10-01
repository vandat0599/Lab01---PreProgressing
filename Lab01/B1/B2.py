import csv
import sys
<<<<<<< HEAD:Lab01/B1/main.py
from CountryOb import *
# first time use source tree to work with GIT.AMAZING~!!
=======
>>>>>>> 44d99f69d1ca2fe522ad150986bac8068beed06c:Lab01/B1/B2.py

# valid command: preprocess --input {inputFilePath} --output {outputFileCSVPath}
argvList = sys.argv
if "--input" in argvList and "--output" in argvList and "preprocess" in argvList and ".csv" in argvList[len(argvList)-1]:
    x = open(argvList[3], encoding='utf-8-sig')
    countries = []
    data = list(x)
    it = iter(data)
    line = next(it)
    try:
        while True:
            country = {}
            lineSplit = line.lstrip().rstrip().split("=")
            country.update({lineSplit[0]: lineSplit[1]})
            line = next(it)
            while "country" not in line:
                lineSplit = line.lstrip().rstrip().split("=")
                country.update({lineSplit[0]: lineSplit[1]})
                line = next(it)
            # remove empty data "country,name,longName,foundingDate,population,capital,largestCity,area"
            if country.get("name") is not None and country.get("longName") is not None and country.get("foundingDate") is not None and country.get("population") is not None and country.get("capital") is not None and country.get("largestCity") is not None and country.get("area") is not None:
                # change mile to km
                area = country["area"]
                if area is not None and "mi" in area and country["country"] != "country":
                    country["area"] = "{}km".format(
                        float(area[0:len(area)-2])*2.59)
                # remove duplicate data
                isDuplicate = False
                for c in countries:
                    # cCopy["country"] = country["country"]
                    if c["name"] == country["name"] and c["longName"] == country["longName"] and c["foundingDate"] == country["foundingDate"] and c["population"] == country["population"] and c["capital"] == country["capital"] and c["largestCity"] == country["largestCity"] and c["area"] == country["area"]:
                        isDuplicate = True
                        break
                if not(isDuplicate):
                    countries.append(country)

    except:
        print("Read data 1 done!!!")

    try:
        with open(argvList[5], 'w') as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=list(countries[0].keys()))
            writer.writeheader()
            for i in range(len(countries)-1):
                writer.writerow(countries[i+1])
    except IOError:
        print("I/O error")
else:
    print(
        "---Command not found\n---Valid command: preprocess --input {Input} --output {Output}\n-----Input: data file (.txt,...)\n-----Ouput: *.csv")
