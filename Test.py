'''
Moataz Khallaf
Combat test
2020/01/21
'''
# imports
import csv, random

# variables, lists and arrays

fil = open("unitStats.csv", newline = "")
readCSV = csv.reader(fil)  # loads file into the csv reader which can read the table row by row

unitStats = []

for line in readCSV:
    unitStats.append(line)

# //*Classes*\\

class NPC:
    def __init__(self, race, tag):
        self.stats = None
        self.race = race
        self.tag = tag

    def getUnitStats(self, statList):
        for i in range(len(statList)):
            if self.race in statList[i][1] and self.tag in statList[i][2]:
                self.stats = unitStats[i]

                '''
                This is to find the unit's stats, it looks for the unit's race then it looks for the
                unit's name, afterwards it returns the stats hopefully sending it
                into the class to create the object and putting it into an array of enemies where
                combat is happening.
                '''

    def useAbility(self):
        print(self.stats)
        choice = input("What would you like to do?")
        for i in range(len(self.stats)):
            if choice == self.stats[i]:
                dmg = random.randrange(1, int(self.stats[9]))
                return dmg




    def returnUnitStats(self):
        return self.stats



class event:
    def __init__(self):
        self.eParty = []
        self.aParty = []

# //*functions*\\
#   linSearch
def linSearch(li, spec):
    for i in range(len(li)):
        print(i, li[i])
        if spec == li[i][1]:
            print("yote")
            break

def unitGrab(li, spec, unit):
    for i in range(len(li)):  # This is to find the unit's stats, it looks for the unit's race then it looks for the
        if spec in li[i][1] and unit in li[i][2]:  # unit's name, afterwards it returns the stats hopefully sending it
            unitStats = li[i]  # into the class to create the object and putting it into an array of enemies where
            return unitStats  # combat is happening.

def menu():
    choice = input('''
    Hello, what would you like to do?
    \t 1. Create a new char
    \t 2. View the Party
    \t 3. Create an encounter
    \t 4. Open quest tracker
    \t 5. Open Summary log
    \t 6. View a Char's stats
     ''')
    return choice

def raceSelect():
    race = input("Race?")
    return race

def tagselect():
    tag = input("tag?")
    return tag

# //*Main*\\

#print(unitGrab(unitStats, raceSelect(), tagselect()))

unit = NPC(raceSelect(), tagselect())
unit.getUnitStats(unitStats)
#print(unit.returnUnitStats())
print(unit.useAbility())