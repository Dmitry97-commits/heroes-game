from character_class import Character
import random



class Khristina(Character):

    def __init__(self, _armor, _damage, _active, _name , _health):
        super().__init__(_name,_damage,_health)
        self._armor = _armor
        self.counter_active = 1
        self.flag_active = False

    def __str__(self):
        return f"{self.name},{self._damage},{round(self._health, 1)},{self.counter_active},{round(self._armor, 1)}"

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

    def attack(self,character):
        self._damage = (self._damage + (self._damage * random.uniform(-0.015, 0.5)))
        character.taking_damage(self._damage)
        if not self.flag_active :
            self.counter_active -= 1
            self.check_flag_active()

        # character._health = character._health - (self._damage + (self._damage * random.uniform(-0.015, 0.05)))
        # return f"Нанесен урон по {character.name}"

    def recovery(self):

        stamina_rec = self._health + (Khristina.health * 0.6)
        if stamina_rec > Khristina.health :
            self._health = Khristina.health
        else:
            self._health = stamina_rec
        if not self.flag_active :
            self.counter_active -= 1
            self.check_flag_active()

    def tortila_mode(self):
        if self._armor > 0:
            self._armor *= 2
        else:
            self._armor = 2
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
