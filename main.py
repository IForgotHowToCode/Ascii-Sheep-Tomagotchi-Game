#Imports
import time
import os
import sys
import json

#Func's
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value 

def typingAscii (text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.08)

def save():

  game_variables = {
    "pet_name": pet_name,
    "energy": energy,
    "hunger": hunger,
    "health": health,
    "training": training,
    "pet_food": pet_food,
    "money": money,
    "animal": animal
  }

  with open("load.json", "w+") as f:
      json_save = json.dumps(game_variables, indent=4)
      f.write(json_save)
#Var's
health = 'good'
energy = 8
hunger = 0
training = 0
pet_food = 10
things_at_store = ('bone', 'yarn', 'sunken boat', 'mini cave', 'fake tree')
done_choosing = False
choice = 0
choice2 = 0
money = 100
animal = 'None'
print("------------------------------------------------------------------------------------------")

words = ("""                                                                   
                                              888                                 
 8888b.  .d8888b   .d8888b 888 888     .d8888b  88888b.   .d88b.   .d88b.  88888b.  
    "88b 88K      d88P"    888 888     88K      888 "88b d8P  Y8b d8P  Y8b 888 "88b 
.d888888 "Y8888b. 888      888 888     "Y8888b. 888  888 88888888 88888888 888  888 
888  888      X88 Y88b.    888 888          X88 888  888 Y8b.     Y8b.     888 d88P 
"Y888888  88888P'  "Y8888P 888 888      88888P' 888  888  "Y8888   "Y8888  88888P"  
                                                                           888      
                                                                           888  """)

for line in words.split('\n'):
   time.sleep(0.2)
   sys.stdout.write(line + '\n')
   sys.stdout.flush()

                                                                           
print("------------------------------------------------------------------------------------------")
time.sleep(1)
typingPrint('Enter pet:')   
print("""
""")
typingPrint('1.Sheep')
print("""
""")

#Choose a pet, repeat until a valid choice is entered.
while done_choosing == False:
 choice = typingInput('Which do you choose? (enter the number)')
 if choice == '1':
   animal = 'Sheep'
   done_choosing = True 
 else:
     typingPrint ('Sorry, that is not a choice. Please enter something else.')
     
#Name pet
pet_name = typingInput ("What do you want to name your pet? ")
print ('Okay, you now have a', animal ,'named', pet_name + '.')
print('')
print ('Your', animal ,'is at', health, 'health right now. You can check it at any time.')

#list choices
print('')
typingPrint('1.Feed your pet')
print('')
typingPrint('2.Buy more food')
print('')
typingPrint('3.Take your pet for a walk')
print('')
typingPrint('4.Play a game with your pet')
print('')
typingPrint('5.Train your pet')
print('')
typingPrint('6.Rest and check stats (pet health, money, etc.)')
print('')
typingPrint('7.Buy a toy for your pet')
print('')
typingPrint("8.Save Game")
print('')
typingPrint("9.Load Game")
#forever loop of things to do

while True:
 print('')
 choice = typingInput('What would you like to do?')

#Feed your pet
 if choice == '1':
  if pet_food > 5:
    if hunger > 0:
      pet_food -= 5
      hunger -= 1
      print("------------------------------------------------------------------------------------------")
      typingPrint('Your pet has been fed!')
      print("------------------------------------------------------------------------------------------")
      print('You now have ', pet_food, ' pet food, and your pets remaining hunger is at ', hunger, '.')
      
    else:
      print("------------------------------------------------------------------------------------------")
      print(pet_name, 'waits next to the food, not eating.')
  else:
    print("------------------------------------------------------------------------------------------")
    typingPrint("You'll need to get some more food first...")

#Buy more food
 elif choice == '2':
     if money > 9:
      money -= 10
      pet_food += 5
      print("------------------------------------------------------------------------------------------")
      print('Food bought! Money = ', money, 'Pet food = ', pet_food)
      print("------------------------------------------------------------------------------------------")

#Take pet for walk
 elif choice == '3':
     if animal == 'Sheep':
       if energy > 5:
         energy -= 3
         hunger += 1 
         print('You go for a nice walk with ' +  pet_name + '. Your pet now has', energy, 'energy and', hunger, 'hunger.')
       else: 
         print('Your', animal, 'seems a bit too tired to go for a walk today.')
     else:
       print('Your', animal, 'stares at you like you are crazy.')

#Play a game
 elif choice == '4':
     if energy > 5:
         energy -= 3
         hunger += 2 
         print('You play with ' + pet_name + '!', pet_name,("now has"), energy, 'energy and', hunger, 'hunger.')

#Train your pet

 elif choice == '5':
     print('')
#Rest your pet and check stats

 elif choice == '6':
     print('')
     typingPrint ('Okay, here are the stats.')
     print('Health:', health)
     print ('Pet energy (0-10):', energy ,)
     print ('Hunger (0 = full 5 = starving):', hunger ,)
     print ('Training (max 10):', training ,)
     print('Pet food:', pet_food)     
     print ('Money:', money ,)
     energy += 2

#Buy a toy
 elif choice == '7':
    print('Here are the items at the store:', things_at_store)

#Save
 elif choice == '8':
  save()

#Load
 elif choice == '9':
  with open('load.json', 'r') as f:
    game_variables = json.load(f)
  

#Input doesn't match any choices
 else:
     typingPrint ('Sorry, that is not a choice. Please enter something else.')