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

    def game(self):

        self.pick_character_in_team()

        counter_of_round = 1

        while self.__team1 and self.__team2:
            if self.__flag_team:
                print("Команда номер 1 начинает раунд -",counter_of_round)
                self.step(self.__team1,self.__team2)
                self.death_kick(self.__team1)
                self.__team1.__str__()
                self.info(self.__team1)

                counter_of_round +=1


            elif not self.__flag_team:
                print("Команда номер 2 начинает раунд -",counter_of_round)
                self.step(self.__team2,self.__team1)
                self.death_kick(self.__team2)
                self.__team2.__str__()
                self.info(self.__team2)

                counter_of_round +=1



        self.__flag_team = not self.__flag_team

    def info(self,team):
        for i in team:
            print(i)



    def death_kick(self,team):      #кик за смерть
        for i in team:
            if i.check_of_death():
                team.remove(i)


    def pick_character_in_team(self):  # добавить инфо
        print(Dima.dima_info)
        print(Khristina.khristina_info)
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
