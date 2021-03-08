from character_class import Character
import random

class Dima(Character):
    _def_name = "Dima"
    _def_st = 500

    def __init__(self,_damage,_active, _name = _def_name,_stamina=_def_st):
        super().__init__(Dima._def_name,_damage,Dima._def_st,_active)


    def attack(self,character):
        damage = (self.damage + (self.damage * random.uniform(-0.05,0.3)))
        if character.armor != 0:
            character.armor = character.armor - damage
            if character.armor < 0:
                character.stamina = character.armor + character.stamina
                character.armor = 0
                return f"Нанесен урон по {character.name}, -{round(damage,1)},броня {round(character.armor,1)} "
            else:
                return f"Нанесен урон по {character.name}, -{round(damage,1)} ,броня {round(character.armor,1)} "


        else:
            character.stamina = character.stamina - damage
            return f"Нанесен урон по {character.name}, -{round(damage),1} ,броня {round(character.armor,1)} "

    def recovery(self):
        stamina_rec = self.stamina + (Dima._def_st * 0.1)
        if stamina_rec > Dima._def_st:
            self.stamina = Dima._def_st
            return self.stamina
        else:
            self.stamina = stamina_rec
            return self.stamina

    def beast_mode(self,character):
        character.stamina = character.stamina - (self.damage * 2)
        return f"Нанесен урон способностью BEAST MODE по {character.name} , - {self.damage * 2} "