from random import randint

class Character:
  def __init__(self):
    self.name = ""
    self.wealth = 100
    self.health = 1
    self.health_max = 1
  def do_damage(self, enemy):
    damage = min(
        max(randint(0, self.health) - randint(0, enemy.health), 0),
        enemy.health)
    enemy.health = enemy.health - damage
    if damage == 0: print ("%s is fleeing from %s." % (self.name, enemy.name))
    else:
        print ("%s is kicking the hell out of %s!" % (self.name, enemy.name))
        if randint(0, 1):
            enemy.loss=randint(1,30)
            enemy.wealth-=enemy.loss
            self.wealth+=enemy.loss
            print("%s lost %d wealth" % (enemy.name, enemy.loss))
    return enemy.health <= 0
