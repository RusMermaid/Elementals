from random import *
from Classes.Elementals.Strikes import *
from Classes.Elementals.Elemental import Elemental

class Airbender(Elemental):
    def __init__(self, name:str, clan:str=None, health:int=None, armor:int=None, strength:float=None, strikes:list = Strike.air_s, is_human:bool=False):
      super().__init__(name, clan, health, armor, strength, strikes, is_human)
      self.clan = "Воздух"
    