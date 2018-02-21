from random import randint
from Character import Character
from Enemy import Enemy
 
class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    #self.wealth = 100
    self.health = 10
    self.health_max = 10
    self.Commands = {'quit': Player.quit,'help': Player.help,'status': Player.status,'rest': Player.rest,'explore': Player.explore,'run': Player.flee,'attack': Player.attack}
  def quit(self):
    print ("%s, the last warrior, lost his way and died of starvation.\nR.I.P." % self.name)
    self.health = 0
  def help(self): print (self.Commands.keys())
  def status(self): print ("%s's health: %d/%d" % (self.name, self.health, self.health_max));print ("%s's wealth: %d" % (self.name, self.wealth))
  def tired(self):
    print ("%s is tired." % self.name)
    self.health = max(1, self.health - 1)
  def rest(self):
    if self.state != 'normal': print ("%s, there's no rest now!" % self.name); self.enemy_attacks()
    else:
      print ("%s rests." % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print ("%s woke up %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s slept more than he should have...!!!" % self.name); self.health = self.health - 1
  def explore(self):
    if self.state != 'normal':
      print ("%s is busy, knock later" % self.name)
      self.enemy_attacks()
    else:
      if randint(0, 1):
        self.extra = randint(1,30)
        self.wealth += self.extra 
        print("%s gained %d wealth" % (self.name, self.extra))
      print ("%s came out of a round maze" % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print ("%s, look who you found:  %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
  def flee(self):
    if self.state != 'fight': print ("%s is running and running in circles" % self.name); self.tired()
    else:
      if randint(0, 1):
        self.loss = randint(1,30)
        self.wealth -= self.loss 
        print("%s lost %d wealth" % (self.name, self.loss))
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s couldn't run much far from %s!" % (self.name, self.enemy.name)); self.enemy_attacks()
  def attack(self):
    if self.state != 'fight': print ("%s just kicking in the thin air." % self.name); self.tired()
    else:
      if self.do_damage(self.enemy):
        print ("%s finally killed %s!" % (self.name, self.enemy.name))
        self.state = 'normal'
        self.wealth += self.enemy.wealth;print("%s gained %d wealth" % (self.name, self.enemy.wealth))
        self.enemy = None
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print ("%s is feeling like Man of Steel!" % self.name)
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self): print ("%s killed the last warrior %s!!!\nR.I.P." %(self.enemy.name, self.name))
