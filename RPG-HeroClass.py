# ============================================================
#  RPG Hero — complete the class below.
#  The class name and method names are already set for you;
#  just fill in the bodies marked with TODO.
# ============================================================

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

        pass

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = "DEAD"
        pass

zeus = Hero("Zeus", 100)
naehlyx = Hero("Naehlyx", 100)

zeus.take_damage(10)
naehlyx.take_damage(1000)

print(f"Zeus's HP: {zeus.hp}")     
print(f"Naehlyx's HP: {naehlyx.hp}")    

