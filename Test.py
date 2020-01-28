'''
Moataz Khallaf
Combat test using pandas
2020/01/27

Contributors: Zeeshan Hooda -> Transitioned to Pandas and refactored for efficiency
'''

# imports
import random
import pandas as pd

# variables, lists and arrays

unit_stats = pd.read_csv('unitStats.csv')

class NPC:
    # I rewrote this method to only require tag and statlist
    # eliminating the need for the idSearch() function
    # because it can just figure out what unit it is
    # in the __init__ method
    def __init__(self, tag, stat_list):
        """
        overview: Class to apply to NPCs and methods are designed to make shit simple but it's not because my coding
        sucks
        :param race:
        :param tag:
        """

        # This loop goes through every unit in the statlist
        # and sets the objects attributes to its respective
        # units attributes based on the tag input
        for unit in range(len(stat_list['TAG'])):
            if stat_list['TAG'][unit].lower() == tag.lower():
                self.tag = tag
                self.race = stat_list.iloc[unit]['RACE']
                self.stats = stat_list.iloc[unit]

    # Since we added the unit stats in the __init__ function
    # I've changed the get_unit_stats to return the unit stats
    # as a pandas dataframe
    def get_unit_stats(self):
        """
        overview: idk fam, like it literally just returns it
        :return:
        """
        return self.stats

    # Honestly this method is a straight copy paste because I
    # do not know what the heck it's supposed to do
    def use_ability(self):
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
                print(dmg)

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
                # added random end range value because it was missing
                # change later to correct range
                dmg = [(random.randint(1, 2))]

        # im guessing you wanted to return the dmg as a value
        # return dmg

    # ### repr and str methods now return the tag name

    def __repr__(self):
        """
        overview: this is just to make sure if I want to print it out, it comes out as a string not an object code
        :return:
        """
        return self.stats['TAG']

    def __str__(self):
        return self.stats['TAG']

class Party:

    # The Party class and respective objects now have
    # an attribute with all the stat_list data so we
    # dont have to load it into memory every time we 
    # add a new unit. It also helps us get rid of the
    # idSearch() function
    def __init__(self, stat_list):
        self.party = []
        self.stat_list = stat_list

    # The unit_comp function now directly gets tag
    # input and creates the unit without having to
    # specify the unit ID or a stat_list (remember
    # we made the stat_list a method for the Party
    # class and now we use it efficiently)
    def unit_comp(self):
        units = int(input("Please enter the # of units you'd like to add: "))
        for _ in range(units):
            # Old version used idSearch() which asked for the id
            # We can just ask for the tag now that were using pandas
            # and we can do it directly inside the class
            unit_tag = input("Please enter a unit tag: ")
            unit = NPC(unit_tag, self.stat_list)
            self.party.append(unit)

    # The old version of this method used another 
    # variable "x" to make the ordered list, but
    # we dont need that because we can do arithmetic
    # inside f-strings
    def take_ability(self, some_input):
        for i in range(len(self.party)):
            print(f" {i+1}. {self.party[i]}")
        
        # I commented this out because it was giving 
        # TypeErrors and I'm not sure what it's for
        # atkChoice = int(input(""))
        input("\nPress [ENTER] to exit... ")

    def __repr__(self):
        return self.party

    def get_unit_comp(self):
        return self.party

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

# IMPORTANT: Because of the refactoring I'm not
#            sure that all of this is necessary
#            anymore.

# //*Main*\\
'''
unitID = idSearch()               -> unit_tag = input("Enter tag: ")
unit1 = NPC(unitID[0], unitID[1]) -> unit1 = NPC(unit_tag, unit_stats) NOTE: Unit stats is a pd dataframe
unit1.getUnitStats(unitStats)     -> No longer needed, stats are set in object creation
unitID = idSearch()               -> unit_tag = input("Enter tag: ")
unit2 = NPC(unitID[0], unitID[1]) -> unit2 = NPC(unit_tag, unit_stats) NOTE: Unit stats is a pd dataframe
unit2.getUnitStats(unitStats)     -> No longer needed, stats are set in object creation
'''

# Added a __name__ == __main__ so this module can
# be imported as well as used as a script for the
# testing purposes
if __name__ == "__main__":
    squad = Party(unit_stats)
    squad.unit_comp()
    squad.take_ability(000)


