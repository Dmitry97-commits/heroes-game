class Character:

    def __init__(self, _name, _damage, _health):
        self._name = _name
        self._damage = _damage
        self._health = _health
        self._counter_active = 1
        self._flag_active = False
        self._max_health = _health
        self._flag_of_death = False


# написать флаг умер или нет



    def __str__(self):
        return f"{self._name},{self._damage},{self._health},{self._counter_active}"

    def taking_damage(self,damage):
        self._health -= damage
        self.check_of_death()

    def attack(self,character):
        character.taking_damage(self._damage)
        if not self._flag_active :
            self._counter_active -= 1
            self.check_flag_active()


    def recovery(self):
        self._health += self._health * 0.3
        if not self._flag_active :
            self._counter_active -= 1
            self.check_flag_active()

    def check_flag_active(self):
        if self._counter_active == 0 :
            self._flag_active = True


    def activate_ability(self,character):
        self.attack(character)
        self._flag_active = False
        self._counter_active = 3


    def check_of_death(self):
        if self._health == 0:
            self._flag_of_death = True
            return True






    @property
    def name(self):
        return self._name
    @property
    def damage(self):
        return self._damage
    @property
    def health(self):
        return self._health
    @property
    def active(self):
        return self._counter_active