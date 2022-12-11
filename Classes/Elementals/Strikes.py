from random import *


class Strike:
  water_s = []
  earth_s = []
  fire_s = []
  air_s = []
  def __init__(self, name:str, clan:str=None, strength:int=None):    
    self.name = name
    if clan is None:
      self.clan = choice(["Земля", "Вода", "Огонь ", "Воздух"])
    else:
      self.clan = clan
		  
    if strength is None:
      self.strength = randint(1, 5)
    else: 
      if int(strength) > 0 and int(strength) <= 10:
        self.strength = strength
      else:
        raise ValueError("Неверное значение силы")
    if clan == "Земля":
      Strike.earth_s.append(self)
    elif clan == "Вода":
      Strike.water_s.append(self)
    elif clan == "Огонь":
      Strike.fire_s.append(self)
    elif clan == "Воздух":
      Strike.air_s.append(self)
    else:
      raise ValueError("Неверный клан")
  def __str__(self):
    return f"{self.name}, {self.clan}, {self.strength}"

w1 = Strike("Ледяная глыба", "Вода", 1)
w2 = Strike("Кольцо холода", "Вода", 3)
w3 = Strike("Цунами", "Вода", 8)
w4 = Strike("Наводнение", "Вода", 5)
w5 = Strike("Гейзер", "Вода", 2)
w6 = Strike("Поток", "Вода", 2)
w7 = Strike("Роса", "Вода", 1)
w8 = Strike("Магия крови", "Вода", 10) #4


e1 = Strike("Землетрясение", "Земля", 6)
e2 = Strike("Валун", "Земля", 1)
e3 = Strike("Обвал", "Земля", 4)
e4 = Strike("Клонирование", "Земля", 9)
e5 = Strike("Каменные шипы", "Земля", 4)
e6 = Strike("Шок земли", "Земля", 3)
e7 = Strike("Стена мечей", "Земля", 2)
e8 = Strike("Извержение", "Земля", 3) #4


f1 = Strike("Армагеддон", "Огонь", 10)
f2 = Strike("Пожар", "Огонь", 1)
f3 = Strike("Огненная ловушка", "Огонь", 1)
f4 = Strike("Дыхание дракона", "Огонь", 5)
f5 = Strike("Поток лавы", "Огонь", 4)
f6 = Strike("Огненный шар", "Огонь", 3)
f7 = Strike("Метеоритный дождь", "Огонь", 5)
f8 = Strike("Стена огня", "Огонь", 3) #4


a1 = Strike("Ураган", "Воздух", 9)
a2 = Strike("Ветер", "Воздух", 1)
a3 = Strike("Тайфун", "Воздух", 8)
a4 = Strike("Левитация", "Воздух", 2)
a5 = Strike("Рой ос", "Воздух", 1)
a6 = Strike("Магическая стрела", "Воздух", 1)
a7 = Strike("Цепь молний", "Воздух", 9)
a8 = Strike("Удушение", "Воздух", 1) #4
