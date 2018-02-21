from random import randint
 
class Character:
  def __init__(self):
    self.name = ""
    self.health = 1
    self.health_max = 1
  def do_damage(self, enemy):
    damage = min(
        max(randint(0, self.health) - randint(0, enemy.health), 0),
        enemy.health)
    enemy.health = enemy.health - damage
    if damage == 0: print ("%s bhaaga %s ke maar pe." % (self.name, enemy.name))
    else: print ("%s marile kela yaak %s!" % (self.name, enemy.name))
    return enemy.health <= 0
 
class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'Crime Master Gogo'
    self.health = randint(1, player.health)
 
class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max = 10
  def quit(self):
    print ("%s ghor pahorilu kela, aaru khaba napai morile.\nR.I.P." % self.name)
    self.health = 0
  def help(self): print (Commands.keys())
  def status(self): print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))
  def tired(self):
    print ("%s'or bhagor lagise." % self.name)
    self.health = max(1, self.health - 1)
  def rest(self):
    if self.state != 'normal': print ("%s, etia aaram nai!" % self.name); self.enemy_attacks()
    else:
      print ("%s rests." % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print ("%s uthale kela yaak %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s besi hui dilu beh!!!" % self.name); self.health = self.health - 1
  def explore(self):
    if self.state != 'normal':
      print ("%s bohut busy pasot aahibi!" % self.name)
      self.enemy_attacks()
    else:
      print ("%s ghuroniya rastat humali kela!!!" % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print ("%s kak palu sa, %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
  def flee(self):
    if self.state != 'fight': print ("%s enei ghuri aasu bal" % self.name); self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s polabu nuwarilu, mari dile kela %s!" % (self.name, self.enemy.name)); self.enemy_attacks()
  def attack(self):
    if self.state != 'fight': print ("%s hawa't urai aaso bal." % self.name); self.tired()
    else:
      if self.do_damage(self.enemy):
        print ("%s mari dilu kela %s!" % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print ("%s koise bom zur aase mur !" % self.name)
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self): print ("%s tapkai dia %s!!!\nR.I.P." %(self.enemy.name, self.name))
 
Commands = {
  'quit': Player.quit,
  'bachao': Player.help,
  'ke bhail ba': Player.status,
  'aaram karo': Player.rest,
  'ghoomo': Player.explore,
  'bhaago': Player.flee,
  'maaro': Player.attack,
  }
 
p = Player()
p.name = input("What is your character's name? ")
print ("(type help to get a list of actions)\n")
print ("%s enters a dark cave, searching for adventure." % p.name)
 
while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print ("%s buji pua nai bal." % p.name)
 
"""
Copyright 2010 Francesco Balducci
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
See <http://www.gnu.org/licenses/> for a copy of the GNU General Public License.
"""