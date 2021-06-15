import collections
import csv
from os import read
from typing import TextIO
from collections import Counter

with open("D:\whitehatjr\Python\Cla-104\SOCR-HeightWeight.csv" , newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)) : 
    num = fileData[i][1]
    newData.append(float(num))

data = Counter(newData)

modeDataRange = {
                    "50-60" : 0,
                    "60-70" : 0,
                    "70-80" : 0,
                                }
for height,occurrence in data.items() : 
    if 50 < float(height) < 60 :
        modeDataRange["50-60"] += occurrence
    elif 60 < float(height) < 70 :
        modeDataRange["60-70"] += occurrence
    elif 70 < float(height) < 80 :
        modeDataRange["70-80"] += occurrence

modeRange,modeOccurrence = 0,0
for range,occurrence in modeDataRange.items() :
    if occurrence > modeOccurrence : 
        modeRange,modeOccurrence = [int(range.split("-")[0]),int(range.split("-")[1])],occurrence

mode = float((modeRange[0]+modeRange[1])/2)
print(mode)
