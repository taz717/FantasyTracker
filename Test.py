'''
Moataz Khallaf
Combat test
2020/01/21
'''
#TODO:
# combat DOT effect
# Find a better way to apply dmg modifier
# PC Port

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
        """
        overview: Class to apply to NPCs and methods are designed to make shit simple but it's not because my coding
        sucks
        :param race:
        :param tag:
        """
        self.stats = None
        self.race = race
        self.tag = tag

    def getUnitStats(self, statList):
        """
        overview: grabbing the unit's stats from a csv file
        input: Unit ID
        output: array with stats
        :param statList:
        :return:
        """
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
        """
        overview: Lets the unit use an ability from the stat list it's assigned
        input: ability choice
        output: ability stats
        :return:
        """
        print(self.stats)
        choice = input("What would you like to do?")
        for i in range(len(self.stats)):
            if choice == self.stats[i] and choice == self.stats[15]:
                dmg = random.randrange(1, int(self.stats[9]))

            elif choice == self.stats[i] and choice == self.stats[16]:  # if the choice and ability match
                dmg = [(random.randrange(1, int(self.stats[9])) * (1 - (self.stats[18] / 100)))
                        , (self.stats[17])
                        , self.stats[19]]  # send back dmg, %chance to apply effect and DOT

            elif choice == self.stats[i] and choice == self.stats[20]:
                dmg = [(random.randrange(1, int(self.stats[9])) * (1 - (self.stats[22] / 100)))
                        , (self.stats[21] / 100)
                        , self.stats[24]
                        ]
            elif choice == self.stats[i] and choice == self.stats[24]:
                dmg = [(random.randint(1, ))]

    def __repr__(self):
        """
        overview: this is just to make sure if I want to print it out, it comes out as a string not an object code
        :return:
        """
        return "%s" % self.stats

    def returnUnitStats(self):
        """
        overview: idk fam, like it literally just returns it
        :return:
        """
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

    def takeAbliity(self, input):
        x = 0
        for i in range(len(self.party)):
            x = x + 1
            print(f" {x}. {(self).party[i]}")

        atkChoice = int(input(""))



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
'''
unitID = idSearch()
unit1 = NPC(unitID[0], unitID[1])
unit1.getUnitStats(unitStats)
unitID = idSearch()
unit2 = NPC(unitID[0], unitID[1])
unit2.getUnitStats(unitStats)
'''

squad = party()
squad.unitComp()
squad.takeAbliity(000)

