from Character import Character
from Enemy import Enemy
from Player import Player
 
p = Player()
p.name = input("What is your character's name? ")
print ("(type help to get a list of actions)\n")
print ("%s enters a dark cave, searching for adventure." % p.name)
 
while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in p.Commands.keys():
      if args[0] == c[:len(args[0])]:
        p.Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print ("%s, your command is not understood!." % p.name)
