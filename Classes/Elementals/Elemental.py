from random import *

from Classes.Elementals.Strikes import Strike

class Elemental:
  elemental = []
  def __init__(self, name:str, clan:str=None, health:int=None, armor:int=None, strength:float=None, strikes:list=None, is_human:bool=False):
    self.name = name
    if is_human is None:
      self.is_human = False
    else: 
      self.is_human = is_human
    if clan is None:
      self.clan = choice(["Земля", "Вода", "Огонь", "Воздух"])
    else:
      if clan in ["Земля", "Вода", "Огонь ", "Воздух"]:
        self.clan = clan
        
      else: 
        raise ValueError("Неверный клан")
    if strikes is None:
      self.strikes.append(choice(Strikes.water_s))
      self.strikes.append(choice(Strikes.water_s))
      self.strikes.append(choice(Strikes.earth_s))
      self.strikes.append(choice(Strikes.earth_s))
      self.strikes.append(choice(Strikes.fire_s))
      self.strikes.append(choice(Strikes.fire_s))
      self.strikes.append(choice(Strikes.air_s))
      self.strikes.append(choice(Strikes.air_s))
    else:
      self.strikes = strikes
    if health is None:
      self.health = randint(10, 100)
    else: 
      if int(health) > 10 and int(health) < 100:
        self.health = health
      else:
        raise ValueError("Неверное значение здоровья")
		  
    if armor is None:
      self.armor = randint(0, 50)
    else: 
      if int(armor) > 0 and int(armor) < 50:
        self.armor = armor
      else:
        raise ValueError("bruhНеверное значение брони")
        
    if strength is None:
      self.strength = uniform(1, 4)
    else: 
      if float(strength) > 0 and float(strength) <= 4:
        self.strength = strength
      else:
        raise ValueError("Неверное значение силы")
    Elemental.elemental.append(self)
  def do_ai_strike(self, el):
    strike = choice(self.strikes)
    strike_strength = self.strength * strike.strength
    el.health -= strike_strength
    print(f"{self.name} ударил {el.name} с силой {strike_strength}")
    if el.health <= 0:
      print(f"{self.name} убил {el.name}")
      Elemental.elemental.remove(el)
      del el
  def do_human_strike(self):
    print(f"aboba Привет, маг {self.clan.lower()}, выбери, кого атаковать:")
    el_name = ""
    [print(i) for i in Elemental.elemental if i.is_human == False]
    while True:
      el = input("Введи имя противника.")
      el_names = [i.name for i in Elemental.elemental if i.name == el]
      if len(el_names) == 0:
        print("Неверное имя. Попробуйте снова.")
      else:
        el_name = el_names[0]
        break 
    el = [i for i in Elemental.elemental if i.name == el_name][0]
    print("Выбери атаку:")
    strike_name = ""
    strikes1 = Strike.earth_s + Strike.air_s + Strike.water_s + Strike.fire_s
    [print(i) for i in strikes1 if i.clan == self.clan]
    strikes = [i for i in strikes1 if i.clan == self.clan]
    while True:
      st = input("Введите название атаки: ")
      st_names = [i.name for i in strikes if i.name == st]
      if len(st_names) == 0:
        print("Неверное название атаки. Попробуйте снова.")
      else:
        st_name = st_names[0]
        break 
    strike_strength = self.strength * [i for i in strikes1 if i.name==st_name][0].strength
    el.health -= strike_strength
    print(f"{self.name} ударил {el.name} с силой {strike_strength}")
    if self.health <= 0:
      print(f"{self.name} убил {el.name}")
      Elemental.elemental.remove(el)
      del el
  @staticmethod
  def game():
    while len(Elemental.elemental) != 1:
      el1 = choice(Elemental.elemental)
      el2 = choice(Elemental.elemental)  
      if el1 == el2:
        continue 
      elif el1.is_human:
        el1.do_human_strike()
      else:
        el1.do_ai_strike(el2)
    else:
      print(f"Победил {el1.name} (стихия: {el1.clan})")
  @staticmethod
  def reset(elementals:list):
    for i in elementals:
      Elemental.elemental.append(i)
  def __str__(self):
    return f"{self.name}, {self.clan}, {self.health}, {self.strength}, {self.armor}"
  