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


    def __repr__(self):
        return "%s" % self.stats

    def returnUnitStats(self):
        return self.stats



class party:
    def __init__(self):
        self.party = []

    def unitComp(self):
        units = int(input("please enter the # of units you'd like to add"))
        for i in range(units):
            unitID = idSearch()
            # grabs unit stats
            unit = NPC(unitID[0], unitID[1])
            # assigns unit stats
            unit.getUnitStats(unitStats)
            self.party.append(unit)
            # adds the unit to the party comp

    def __repr__(self):
        return "%s" % self.party

    def returnUnitComp(self):
        return self.party

# //*functions*\\

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

def idSearch():
    id = (input("Please enter race ID"))
    for i in range(len(unitStats)):
        if id == (unitStats[i][0]):
            race = unitStats[i][1]
            tag = unitStats[i][2]
            return race, tag


# //*Main*\\
squad = party()
squad.unitComp()
print(squad.returnUnitComp())