# FantasyTracker
This program is made for my homebrew dnd that mixes warhammer lore with darkest dungeon type combat

## Quest Tracker (anyone)

### class: used to setup quests and shtuff.

#### Must be able to:

1) create quest objects which have a goal and rewards
2) have attributes such as reward == *whatever the reward is*\
Description == *quest objective*\
goal == *summary of quest description*
3) end when objective is complete dividing the reward up to the party

## Combat System (Taz)

### Stat tracker

1) create a csv with stats for every enemy required
2) pull from the stats into a class that creates enemeies as objects
3) grab stats for parties which are arrayed together.
4) display all stats (abilities too because screw khalil)

### Combat maths

1) calculate how much dmg an object should do\
a) melee dmg\
b) melee str\
c) AP
2) calculate how much dmg an object should take in return\
a) ward sav and res\
b) armor vs toughness
3) delete objects with 0 hp
4) accuracy and prot is minimum -> random between min and 100

## Character (Taz)

### new char type beat

Just instantly roll for everything and sauce it in a class to create a character object

## Summary Log (anyone)

At the end of every session, there should be an option to summarize everything that's happened
It's just an input that's gets written on a file every time the session ends
