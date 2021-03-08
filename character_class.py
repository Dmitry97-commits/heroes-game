class Character:
    def __init__(self,_name,_damage,_stamina,_active):
        self.name = _name
        self.damage = _damage
        self.stamina = _stamina
        self.active = _active


    def __str__(self):
        return f"{self.name},{self.damage},{self.stamina},{self.active}"


    def attack(self,character):
        self.stamina = self.stamina - self.damage
        return self.stamina

    def recovery(self):
        self.stamina =self.stamina + (self.stamina * 0.3)
        return self.stamina
