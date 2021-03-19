from character_class import Character
import random

class Dima(Character):

    def __init__(self,_damage, _name, _health):
        super().__init__(_name, _damage, _health)
        self.__k_damage = 1 #кэф атаки


    def __str__(self):
        return f"{self._name},{self._damage},{self._health},{self.counter_active}"


    def attack(self,character):
        self._damage = (self._damage + (self._damage * random.uniform(-0.05, 0.3))) * self.__k_damage
        character.taking_damage(self._damage)
        if not self.flag_active :
            self.counter_active -= 1
            self.check_flag_active()


    def recovery(self):# добавить макс значение стамины , на данный момент , поменять стамину на хэлс
        max_health = self._health
        stamina_rec = self._health + (max_health * 0.1)
        if stamina_rec > max_health:
            self._health = max_health
            if not self.flag_active :
                self.counter_active -= 1
                self.check_flag_active()
        else:
            self._health = stamina_rec
            if not self.flag_active :
                self.counter_active -= 1
                self.check_flag_active()


    def activate_ability(self,character): # блокировка
        self.__k_damage = 3
        self.attack(character)
        self.__k_damage = 1
        self.flag_active = False
        self.counter_active = 3

    def check_flag_active(self):
        if self.counter_active == 0 :
            self.flag_active = True

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


# h1 = Dima(0,2,1,"da",300)
# print(h1.health)
# h1.taking_damage(100)
# print(h1.health)

