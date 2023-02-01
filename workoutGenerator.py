#Create a program to generate a workout

import random
import csv
from datetime import date
import time
#import numpy as np

arms = ['Bicep Curls', 'Diamond Push-ups', 'Push-ups', 'Tricep Push-ups', 'Pike Push-ups' ]
legs = ['One Leg Squats', 'Jump Squats', 'Crouch Walk', 'Calf Raises', 'Regular Squats']

date = date.today()
personToWorkout = input("Enter your Name: ")
weight = int(input("Enter your weight: "))
print("Daily Reminder: Stretching is Just as Important.")
bodySetChoice = str(input("What would you like to workout? Enter either: (Arms) / (Legs)  "))
#bodySetChoice = input("1. Arms / 2. Legs / Input the number: ")

if bodySetChoice == "Arms" or "arms":
    #results = print(random.choice(arms) + " "+ (random.randrange(1, 25, 5)))
    results1 = random.choice(arms)
    results2 = random.randrange(1,25,5)
    print(results1, results2)
elif bodySetChoice == "Legs" or "legs":
    #results = print(random.choice(legs) + " " + str(random.randrange(1,25, 5)))
    results1 = str(random.choice(legs))
    results2 = int(random.randrange(1,25,5))
    print(results1, results2)


moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())    
with open("Results"+moment+'.txt', 'w') as f:
    f.write(str(date))
    f.write("\n")
    f.write(personToWorkout)
    f.write("\n")
    f.write(str(weight))
    f.write("\n")
    f.write("BodySetChoice is: " + str(bodySetChoice))
    f.write("\n")
    f.write(results1)
    f.write("\n")
    f.write(str(results2))
    
 