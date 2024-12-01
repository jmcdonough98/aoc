from math import inf
class WizardSim():

    def __init__(self,hp,mana,bhp,bdam,manaspent=0,shield=0,poison=0,recharge=0,hm=False):
        self.hp = hp
        self.mana = mana 
        self.manaspent = manaspent
        self.bhp = bhp 
        self.bdam = bdam

        # turns left
        self.shield = shield 
        self.poison = poison
        self.recharge = recharge

        self.spells = {0:self.MagicMissle, 1: self.Drain, 2:self.Shield, 3:self.Poison, 4:self.Recharge}
        self.hm = hm

    # instant
    def MagicMissle(self): # 13.25 mana/damage
        if self.mana >= 53:
            self.mana -= 53
            self.manaspent += 53 
            self.bhp -= 4
            return 1
        return 0 # failed
    # instant
    def Drain(self): #36.5 mana/damage
        if self.mana >= 73:
            self.mana -= 73
            self.manaspent += 73 
            self.bhp -= 2 
            self.hp += 2
            return 1
        return 0 #failed
    # effect
    def Shield(self): 
        if self.shield == 0 and self.mana >= 113:
            self.shield = 6
            self.mana -= 113 
            self.manaspent += 113 
            return 1
        return 0
    # effect
    def Poison(self): # 173 mana, 3 dam/turn for 6 turns = 9.6 mana/damage
        if self.poison == 0 and self.mana >= 173:
            self.poison = 6
            self.mana -= 173
            self.manaspent += 173
            return 1 
        return 0
    # effect
    def Recharge(self):
        if self.recharge == 0 and self.mana >= 229:
            self.recharge = 5
            self.mana -= 229
            self.manaspent+= 229
            return 1
        return 0
    def applyEffects(self):
        if self.poison > 0:
            self.bhp -= 3
            self.poison -= 1
        if self.recharge > 0:
            self.mana += 101
            self.recharge -= 1
        if self.shield > 0:
            self.shield -= 1

    # 1 = victory, 0 = defeat or invalid turn, None = valid turn
    def turn(self,spell):
        # Player Turn
        if self.hm:
            self.hp -= 1
            if self.hp == 0:
                return 0
        self.applyEffects()
        if self.bhp <= 0:
            return 1
        res = (self.spells[spell])()
        if res != 1:
            print("oops")
            return 0
        if self.bhp <= 0:
            return 1
        # Boss Turn
        self.applyEffects()
        if self.bhp <= 0:
            return 1
        self.hp -= (self.bdam - (int(self.shield != 0)*7))
        if self.hp <= 0:
            return 0
   
    def castable_spells(self):
        castable = []
        if self.mana >= 53:
            castable.append(0)
        if self.mana >= 73:
            castable.append(1)
        if self.shield <= 1 and self.mana >= 113:
            castable.append(2)
        if self.poison <= 1 and self.mana >= 173:
            castable.append(3)
        if self.recharge <= 1 and self.mana >= 229:
            castable.append(4)
        return castable

def recursiveSolution(W, spell):
    global minVal 
    res = W.turn(spell)
    if W.manaspent > minVal:
        return inf
    if res == 1:
        if W.manaspent < minVal:
            minVal = W.manaspent
        return W.manaspent
    if res == 0:
        return inf
    tmp = [recursiveSolution(WizardSim(W.hp,W.mana,W.bhp,W.bdam,W.manaspent,W.shield,W.poison,W.recharge,W.hm),spell) for spell in W.castable_spells()] + [inf]
    return min(tmp)

def part1():
    return min(recursiveSolution(WizardSim(50,500,51,9),i) for i in range(5))

def part2():
    return min(recursiveSolution(WizardSim(50,500,51,9,hm=True),i) for i in range(5))

if __name__ == "__main__":
    minVal = inf
    print("Part 1:", part1())
    minVal = inf
    print("Part 2:",part2()) 
