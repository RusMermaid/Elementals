from Classes.Elementals.Elemental import Elemental
from Classes.Elementals.Mages.Airbender import Airbender
from Classes.Elementals.Mages.Earthbender import Earthbender
from Classes.Elementals.Mages.Firebender import Firebender
from Classes.Elementals.Mages.Waterbender import Waterbender




a = Airbender("Bruh", is_human=True)
e = Earthbender("Cringe")
f = Firebender("Herald")
w = Waterbender("Cronch")

a2 = Airbender("Arina2")
e2 = Earthbender("Cringe2")
f2 = Firebender("Herald2")

ai1 = 0
ei1 = 0
fi1 = 0
wi1 = 0


for i in range(1):
  Elemental.game()
  if Elemental.elemental[0].clan == "Вода":
    wi1 += 1
    Elemental.reset([a, e, f])
  elif Elemental.elemental[0].clan == "Воздух":
    ai1 += 1
    Elemental.reset([e, f, w])
  elif Elemental.elemental[0].clan == "Земля":
    ei1 += 1
    Elemental.reset([a, f, w])
  elif Elemental.elemental[0].clan == "Огонь":
    fi1 += 1
    Elemental.reset([a, e, w])
#print(f"Вода {wi1},\nЗемля{ei1},\nОгонь{fi1},\nВоздух{ai1}.")
