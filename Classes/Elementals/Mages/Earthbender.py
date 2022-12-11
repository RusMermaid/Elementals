from random import *
from Classes.Elementals.Strikes import *
from Classes.Elementals.Elemental import Elemental

class Earthbender(Elemental):
  def __init__(self, name:str, clan:str=None, health:int=None, armor:int=None, strength:float=None, strike:list = Strike.earth_s, is_human:bool=False):
      super().__init__(name, clan, health, armor, strength, strike, is_human)
      self.clan = "Земля"