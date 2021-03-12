from character_class import Character
import random

class Dima(Character):

    def __init__(self, _armor, _damage, _active, _name, _health):
        super().__init__(_name, _damage, _health)
        self.__k_damage = 1 #кэф атаки
        self._armor = _armor
        self.counter_active = 1
        self.flag_active = False

    def __str__(self):
        return f"{self._name},{self._damage},{self._health},{self.counter_active}"

    def taking_damage(self,damage):
        if self._armor == 0:
            self._health -= damage
        elif self._armor > 0:
            self._armor -= damage
            if self._armor < 0:
                self._health = self._armor + self._health # если после получения урона броню , она стала минусовой то урон прибавляется к стамине
                self._armor = 0
            else:
                self._health -= damage
        else:
            self._health -= damage


    def attack(self,character):#переписать
        self._damage = (self._damage + (self._damage * random.uniform(-0.05, 0.3))) * self.__k_damage
        character.taking_damage(self._damage)
        if not self.flag_active :
            self.counter_active -= 1
            self.check_flag_active()


    def recovery(self):# добавить макс значение стамины , на данный момент , поменять стамину на хэлс
        stamina_rec = self._health + (Dima.health * 0.1)
        if stamina_rec > Dima.health:
            self._health = Dima.health
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
        return self.counter_active
