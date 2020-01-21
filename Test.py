'''
Moataz Khallaf
Combat test
2020/01/21
'''
# imports
import csv

# variables, lists and arrays

fil = open("unitStats.csv", newline = "")
readCSV = csv.reader(fil)  # loads file into the csv reader which can read the table row by row

unitStats = []

for line in readCSV:
    unitStats.append(line)

# functions

def unitSpawn(unit):
    for i in range(len(unitStats)):
        if unit == unitStats[i][1]:

