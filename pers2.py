from character_class import Character
import random



class Khristina(Character):

    def __init__(self, _armor, _damage, _name , _health):
        super().__init__(_name,_damage,_health)
        self._armor = _armor
        self._max_armor = _armor





    def __str__(self):
        return f"{self.name},{self._damage},{round(self._health, 1)},{self._counter_active},{round(self._armor, 1)}"

    def taking_damage(self,damage):
        if self._armor == 0:
            self._health -= damage
        elif self._armor > 0:
            self._armor -= damage
            if self._armor < 0:
                self._health = self._armor + self._health # если после получения урона броню , она стала минусовой то урон прибавляется к стамине
                self._armor = 0

    def attack(self,character):
        self._damage = (self._damage + (self._damage * random.uniform(-0.015, 0.5)))
        character.taking_damage(self._damage)
        if not self._flag_active :
            self._counter_active -= 1
            self.check_flag_active()

        # character._health = character._health - (self._damage + (self._damage * random.uniform(-0.015, 0.05)))
        # return f"Нанесен урон по {character.name}"

    def recovery(self):
        stamina_rec = self._health + (self._max_health * 0.6)
        if stamina_rec > self._max_health :
            self._health = self._max_health
        else:
            self._health = stamina_rec
        if not self._flag_active :
            self._counter_active -= 1
            self.check_flag_active()

    def activate_ability(self,character):
        if self._armor > 0:
            self._armor = 2 * self._max_armor
        else:
            self._armor = self._max_armor
        self._flag_active = False
        self._counter_active = 3


    def check_flag_active(self):
        if self._counter_active == 0 :
            self._flag_active = True


    @property
    def name(self):
        return self._name
    @property
    def damage(self):
        return self._damage
    @property
    def stamina(self):
        return self._health
    @property
    def active(self):
        return self._counter_active

if __name__ == "__main__":
    pers = Khristina(100,50,"aaa",200)
    print(pers)
    pers.taking_damage(110)
    print(pers)
    pers.recovery()
    print(pers)







