import os
from time import sleep
from random import randint
magic=["A ball of fire shoots from your palm at the target",
        "Arcs of lightning lash out at the monster","A wave of pure energy is unleashed at the monster"]
class Monster(object):
  def __init__(self, name,max_hp,says,desc,hp=0):
    self.name = name
    self.hp = hp
    self.max_hp= max_hp
    self.says = says
    self.hp=self.max_hp
    self.desc=desc
  def get_desc(self):
    return self.desc
  def take_dmg(self,damage=0):
    if damage!=0:#the hoops I jump through to avoid writing another function...
      print(f'The {self.name} takes {damage} points of damage.\n')
      self.hp-=damage
      if self.hp<0:
        self.hp=0
      print(f'It now has {self.hp} HP left')
    
    if self.hp<0:
      self.hp=0
    
    if self.hp<1:
      if damage!=0:
        print("You've defeated the monster")
      return 1 #remember to use this when attacking later
  def get_name(self):
    return self.name
  def speak(self):
    if self.hp<self.max_hp:#angry noise
      print(self.says[1])
    else:
      print(self.says[0])
  def set_desc(self,new_description):
    self.desc=new_description
  def show_hp(self):
    print("It has",self.hp,"HP")
  def instance(self):#function for every monster appearance
    print(f'A {self.name} appears, it has {self.hp} hit points')
  def fight(self):
    while True:
      weap=input("Are you using a sword, a bow or magic?\n").lower()
      if weap[0]=="s":
        print("You draw your sword")
        return weap
      elif weap[0]=="b":
        print("You aim your bow")
        return weap
      elif weap[0]=="m":
        print("Magical energy crackles between your fingers")
        return weap
      else:
        print("That was never an option")
  def practise(self):
    while True:    
      turns=0
      if True:
        
        os.system('cls' if os.name == 'nt' else 'clear')
      #Clears the console
        while self.take_dmg()!=1:
          print("The monster says",end=' ')
          self.speak()
          sleep(1)
          choice=self.fight()
          choice=choice[0]
          sleep(1)
          dmg=randint(1,8)
          if choice=="s":
            print("You swing at the beast")
            self.take_dmg(dmg)
          elif choice=="b":
            print("You fire an arrow at the creature")
            self.take_dmg(dmg)
          else:
            mag=randint(0,2)
            print(magic[mag])
            self.take_dmg(dmg)
          sleep(1)
          turns+=1
          if self.take_dmg()==1:
            return 1

  

class Friend(Monster):
  def __init__(self, name,max_hp,says,desc,high5_say,gift,hp=0):
    super().__init__(name,max_hp,says,desc,hp)
    self.gift=gift
    self.high5_say=high5_say
  def get_gift(self):
    return self.gift
  def get_high5(self):
    return self.high5_say
  def set_gift(self,gift):
    self.gift=gift
  def set_high5(self,new_line):
    self.high5_say= new_line
  def highfive(self):
    print(self.name+' raises an apendage and says')
    print(self.high5_say)
    print(self.name,"gives you a "+self.gift)
  def fight(self):
    print("You've decided to attack")
    print(self.name,"cowers")
    while True:
      weap=input("Are you using a sword, a bow or magic?\n").lower()
      if weap[0]=="s":
        print("You draw your sword")
        return weap
      elif weap[0]=="b":
        print("You aim your bow")
        return weap
      elif weap[0]=="m":
        print("Magical energy crackles between your fingers")
        return weap
      else:
        print("That was never an option")
  def encount_frond(self,picked):
    
    turns=0
    if picked=="attacking":
      
      os.system('cls' if os.name == 'nt' else 'clear')
    #Clears the console
      while self.take_dmg()!=1:
        print("The monster says",end=' ')
        self.speak()
        sleep(1)
        choice=self.fight()
        choice=choice[0]
        sleep(1)
        dmg=randint(1,8)
        if choice=="s":
          print("You swing at the beast")
          self.take_dmg(dmg)
        elif choice=="b":
          print("You fire an arrow at the creature")
          self.take_dmg(dmg)
        else:
          mag=randint(0,2)
          print(magic[mag])
          self.take_dmg(dmg)
        sleep(1)
        turns+=1

        if turns==5 and self.take_dmg()!=1:
          print(f"The {self.name} has escaped")
          return 0
        if turns<3:
          if input("Do want to continue your attack?(y/n)\n").lower()=="n":
            break
        if self.take_dmg()==1:
          return 1
    
    if self.take_dmg()==1:
      return 1
      print("The monster says",end=' ')
      self.speak()
      if self.hp<self.max_hp:
        print("You apologize for attacking\nThe monster seems to calm down")
    self.highfive()
    return 2


class Enemy(Monster):
  def __init__(self,name,max_hp,says,desc,weakness,fight_say,hp=0):
    super().__init__(name,max_hp,says,desc,hp)
    self.fight_say=fight_say
    self.weakness=weakness
  def set_weakness(self,weak):
    self.weakness=weak
  def set_fight_words(self,fighting):
    self.fight_say=fighting
  def fightingwords(self):
    return self.fight_say
  def fight(self):
    print(self.name+"looks ready to fight\n"+self.fight_say)
    while True:
      weap=input("Are you using a sword, a bow or magic?\n").lower()
      if weap[0]=="s":
        print("You draw your sword")
        break
      elif weap[0]=="b":
        print("You aim your bow")
        break
      elif weap[0]=="m":
        print("Magical energy crackles between your fingers") 
        break
      else:
        print("That was never an option")
    if weap[0]==self.weakness:
      return weap,1
    else:
      return weap,0
  def encount_anemone(self,picked):
    turns=0
    if picked=="h5":
      print("You approach the monster arm raised to give it a highfive")
      sleep(3)
      self.fightingwords()
      print("The creature attacks you while your guard is down")
      print('''
                ____              ___      ____   ____
        \   /  |    |  |    |    |   \  |  |     |    \ \n         \ /   |    |  |    |    |    | |  |__   |     |
          |    |    |  |    |    |    | |  |     |     |
          |    |____|  |____|    |___/  |  |___  |____/    
                                      
                                        ''')
      return 0
    elif picked=="attacking":
      os.system('cls' if os.name == 'nt' else 'clear')
    #Clears the console
      while self.take_dmg()!=1:
        print("The monster says",end=' ')
        self.speak()
        sleep(1)
        choice,weak=self.fight()
        choice=choice[0]
        sleep(1)
        dmg=randint(1,8)
        if weak==1:
          dmg*=2
        if choice=="s":
          print("You swing at the beast")
          self.take_dmg(dmg)
        elif choice=="b":
          print("You fire an arrow at the creature")
          self.take_dmg(dmg)
        else:
          mag=randint(0,2)
          print(magic[mag])
          self.take_dmg(dmg)
        sleep(1)
        turns+=1
        print("The monster swings at you",end=' ')
        if turns<10:
          print("but you barely dodge")
        else:
          print("and lands a crushing blow")
          print('''
                ____              ___      ____   ____
        \   /  |    |  |    |    |   \  |  |     |    \ \n         \ /   |    |  |    |    |    | |  |__   |     |
          |    |    |  |    |    |    | |  |     |     |
          |    |____|  |____|    |___/  |  |___  |____/    
                                      
                                        ''') 
          return 0

def encounter(mon):
  mon.instance()
  nature=type(mon)
  while True:
    print('''|Look at the monster|Talk to the monster |
|Attack the monster |Highfive the monster|''' )
    do= input("What would you like to do\n").lower()
    try:
      
      do=do[0]
    except:
      print("Welp we default to sword in this game")
      do='s'
    if do=="l":
      print(mon.get_desc())
      
    elif do=="t":
      input("What would you like to say\n")
      print("The monster says",end=' ')
      mon.speak()
      sleep(1)
      print("You don't think it speaks your language")
      
    elif do=="a":
      if nature is Friend:
        end=mon.encount_frond("attacking")
      else:
        end=mon.encount_anemone("attacking")
      break
    elif do=="h":
      if nature is Enemy:
        end=mon.encount_anemone("h5")
      else:
        end=mon.encount_frond("h5")
      break
    
  if end==0:
    sleep(4)
    print("An unfortunate end")
    sleep(1)
    print("But was it due to misfortune?\nOr your own choices")
    sleep(1)
    print("better luck next time")
    return 0
  if end==1:
    print("Having defeated the",mon.name,"you feel a sense of accomplishment")
    return 1
  if end==2:
    print("You smile and watch the creature leave")
    sleep(1)
    print("Hopefully, you've made a new friend")




      