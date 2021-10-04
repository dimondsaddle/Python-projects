from random import randint 
from monst import Monster,Friend,Enemy ,encounter
from time import sleep#important for suspense
import os
#monster needs a name, maxhp, and 2 phrases 1 for early 1 for late 
#if friend, give it extra line for high5 and a gift
#if foe, needs an attacking sound and a weakness(sword(s), bow(b) or magic (m) )
magic=["A ball of fire shoots from your palm at the target",
        "Arcs of lightning lash out at the monster","A wave of pure energy is unleashed at the monster"]
Cacty=Friend("Cactuar",15,["*Boincing noise*","*Angry whistle noise*",],"A 2ft tall cactus looking creature, it seems to enjoy running","Buyong","Thorn")
Cacty.get_desc()
print("Welcome")

big_C=Enemy("Giant Cactuar",90,["'Bwuooooo'","*Deafening whistle noise*"],"A 30 ft tall monster of a Cactuar, it seems you've made it angry","m"," ")
#more monsters needed

target_dummy=Monster("Scarecrow",20,["nothing but just stares at you, motionless","nothing"],"It's a fish")





print("Welcome to the world of cactus shaped monsters and more.\n")
print("Try and befriend those that are kind and defeat those that aren't.")
sleep(1)
print("But beware, there are some challenges that need not be faced")

print("You decide to practise your skills on the farm's scarecrow")
sleep(2)
target_dummy.practise()
print("Feeling accomplished, you head into the world in search of monsters")
sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')
cact= encounter(Cacty)
if cact==1:
  encounter(big_C)
  