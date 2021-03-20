from character_class import Character
from pers1 import Dima
from pers2 import Khristina


# каунтер для характеров в тиме
# тим 1 - тим 2 - пустой список
# статич методы для выбора
# методы для ходьбы
class Game:

    def __init__(self, counter_of_characters):
        self.__counter_of_characters = counter_of_characters
        self.__team1 = []
        self.__team2 = []
        self.__flag_team = True  # если тру - то 1ая , фолс - 2ая

    def game(self): #какая команда должна ходить ,1)  2)проверка .step t1 , t2 flag t not flag t 3) у каждого из перс поле умер или нет.
        # ф-ия  после каждого тэкинг дамаг - ок .не ок

        self.pick_character_in_team()     # начало игры


        while self.__flag_team:
            print("Команда номер 1 делает первый ход !")
            self.step(self.__team1,self.__team2)
            self.death_kick(self.__team1)
            if self.dead_team(self.__team1): # завершение игры в случае смерти всех членов команды
                print("Команда 1 проиграла")
                self.__flag_team = False       # право начать след. игру команде победителя
                break                       # ?


            print("Команда номер 2 делает первый ход !")
            self.step(self.__team2,self.__team1)
            self.death_kick(self.__team2)
            if self.dead_team(self.__team2):
                print("Команда 2 проиграла")
                self.__flag_team = True
                break


            self.__flag_team = False


        while not self.__flag_team:
            print("Команда номер 2 делает первый ход !")
            self.step(self.__team2,self.__team1)
            self.death_kick(self.__team2)
            if self.dead_team(self.__team2):
                print("Команда 2 проиграла")
                self.__flag_team = True
                break

            print("Команда номер 1 делает первый ход !")
            self.step(self.__team1,self.__team2)
            self.death_kick(self.__team1)
            if self.dead_team(self.__team1):
                print("Команда 1 проиграла")
                self.__flag_team = False
                break

            self.__flag_team = True


    def death_kick(self,team):      #кик за смерть
        for i in team:
            if i.check_of_death():
                team.remove(i)


    def dead_team(self,team):    #проверка на наличие игроков в команде
        if len(team) == 0 :
            return True


    def pick_character_in_team(self):  # добавить инфо
        while len(self.__team1) < self.__counter_of_characters:
            num_ch = int(input("Номер персонажа : "))
            if num_ch == 1:
                pers1 = Dima(50, "dima", 400)
                self.add_character_in_team(pers1)
            elif num_ch == 2:
                pers2 = Khristina(100, 20, "khristina", 600)
                self.add_character_in_team(pers2)

        self.__flag_team = False

        while len(self.__team2) < self.__counter_of_characters:
            num_ch = int(input("Номер персонажа : "))
            if num_ch == 1:
                pers1 = Dima(50, "dima", 400)
                self.add_character_in_team(pers1)
            elif num_ch == 2:
                pers2 = Khristina(100, 20, "khristina", 600)
                self.add_character_in_team(pers2)

        self.__flag_team = True

    def add_character_in_team(self, character):
        if self.__flag_team:
            self.__team1.append(character)

        else:
            self.__team2.append(character)



    def step(self, team , team2):
        character_choice = int(input("Выбери перс : "))  # 1,2,3

        pers = team[character_choice - 1]

        if pers.check_flag_active():
            step_choice = int(input("Выбери действие : 1) Атака 2) Пополнение здоровья 3) Использование способнности"))  # активность,атак,восст

        else :
            step_choice = int(input("Выбери действие : 1) Атака 2) Пополнение здоровья"))  # активность,атак,восст
        if step_choice == 1 or step_choice == 3:
            choice_of_enemy = int(input("Выбери цель : "))
            if step_choice == 1 :
                pers.attack(team2[choice_of_enemy - 1])
            else:
                pers.activate_ability(team2[choice_of_enemy - 1])
        elif step_choice == 2 :
            pers.recovery()







# написать фун-ю хода . ВЫБОР перс Выбор Хода (атака и тд ) not flag_team (цикл) + ПРОВЕРКА НА СМЕРТЬ
