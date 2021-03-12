class Character:

    def __init__(self, _name, _damage, _health):
        self._name = _name
        self._damage = _damage
        self._health = _health
        self.counter_active = 1
        self.flag_active = False






    def __str__(self):
        return f"{self._name},{self._damage},{self._health},{self.counter_active}"

    def taking_damage(self,damage):
        self._health -= damage

    def attack(self,character):
        character.taking_damage(self._damage)
        if not self.flag_active :
            self.counter_active -= 1
            self.check_flag_active()


    def recovery(self):
        self._health += self._health * 0.3
        if not self.flag_active :
            self.counter_active -= 1
            self.check_flag_active()

    def check_flag_active(self):
        if self.counter_active == 0 :
            self.flag_active = True


    def activate_ability(self,character):
        self.attack(character)
        self.flag_active = False
        self.counter_active = 3






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
        return self.counter_active