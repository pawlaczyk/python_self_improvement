import random
import math

class Warrior:
    def __init__(self, name="Warrior", health=0,
                 attk_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attk_max = attk_max
        self.block_max = block_max

    def attack(self):
        attk_amt = self.attk_max * (random.random() + .5)
        return attk_amt

    def block(self):
        block_amt = self.block_max * (random.random() + .5)
        return block_amt


class Battle:
    def start_fight(self, warior1, warior2):
        while True:
            if self.get_attack_result(warior1, warior2) == "Game Over":
                break # umar jeden z wojownikow
            if self.get_attack_result(warior2, warior1) == "Game Over":
                break # umar jeden z wojownikow

    def get_attack_result(self, wariorA:Warrior, wariorB:Warrior):
        warior_a_attk_amt = wariorA.attack()
        warior_b_block_amt = wariorB.block()
        damage_2_warior_b = math.ceil(warior_a_attk_amt - warior_b_block_amt)
        wariorB.health -= damage_2_warior_b
        print("{} attacks {} and deals {} damage".format(
            wariorA.name, wariorB.name, damage_2_warior_b))
        print("{} id down to {}".format(wariorB.name, wariorB.health))

        if wariorB.health <= 0:
            print("{} has died and {} is Wictorius".format(wariorB.name, wariorA.name))
            return "Game Over"
        else:
            return "Fight again"


def main():
    thor = Warrior("Thor", 50, 20, 10)
    loki = Warrior("Loki", 50, 20, 10)

    battle = Battle()
    battle.start_fight(thor, loki)

main()