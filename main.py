"""
Date: 11/17/2019
Authour: Moataz Khallf & Dhiraj Meenavilli
Title: Fantasy Tracker
"""
Log = 'Log.txt'
"""
try:
    open(Log,'x')

except:
    open(Log,'r')
"""
### ------------------------------ Quest Tracker --------------------------------- ###
class Quest:
    def __init__(self,description, goal, reward):
        self.des = description
        self.goal = goal
        self.reward = reward

    def get_des(self):
        return self.des

    def get_goal(self):
        return self.goal

    def get_reward(self):
        return self.reward

    def set_goal(self,new_goal):
        self.goal = new_goal

    def set_reward(self,new_reward):
        self.reward = new_reward
### ------------------------------ Combat System --------------------------------- ###

### ------------------------------ Charachter ------------------------------------ ###

### ------------------------------ Summary Log ----------------------------------- ###

#def log(event):
f = open(Log, "w")
f.write("Now the file has more content!")
f.close()

