

import numpy as np
import random
import pandas as pd
def roll(num_dice):
    rolls=[]
    for i in range(num_dice):
        dice_roll=random.randint(1,6)
        rolls.append(dice_roll)
    return(np.array(rolls))

#test 
number_of_die=5

roll_1=roll(number_of_die)
#Taking the indexes
take_1 = [0,0,1,0,0]
keep_1=np.take(roll_1, take_1)

number_of_die=number_of_die-keep_1.size

if(number_of_die>0):
    roll_2=roll(number_of_die)
    take_2 = 0
    keep_2=np.take(roll_2, take_2)

number_of_die=number_of_die-keep_2.size

if(number_of_die>0):
    roll_3=roll(number_of_die)
    keep_3=roll_3


hand=np.append(keep_1,keep_2)
hand=np.append(hand,keep_3)

bet="chancen"



print('end')