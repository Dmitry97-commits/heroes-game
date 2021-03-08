from character_class import Character
import random



class Khristina(Character):
    def_name = "Khristina"
    def_st = 500
    def __init__(self,_armor,_damage,_active,_name = def_name,_stamina = def_st):
        super().__init__(Khristina.def_name,_damage,Khristina.def_st,_active)
        self.armor = _armor

    def __str__(self):
        return f"{self.name},{self.damage},{round(self.stamina,1)},{self.active},{round(self.armor,1)}"

    def attack(self,character):
        character.stamina = character.stamina - (self.damage + (self.damage * random.uniform(-0.015,0.05)))
        return f"Нанесен урон по {character.name}"

    def recovery(self):
        stamina_rec = self.stamina + (Khristina.def_st * 0.6)
        if stamina_rec > Khristina.def_st :
            self.stamina = Khristina.def_st
            return self.stamina
        else:
            self.stamina = stamina_rec
            return self.stamina

    def tortila_mode(self):
        if self.armor > 0:
            self.armor = self.armor * 2
            return self.armor
        else:
            self.armor = 1 * 2
            return self.armor
