import random

rickPictures = [
  "Surprised Rick",
  "Special Needs Rick",
  "Flirty Rick",
  "Romantic Rick",
  "Sexual Predator Rick", 
  "Imaginary Burger Rick",
  "Model Rick",
  "Visionary Rick",
  "Fonz Rick",
  "Party Rick",
  "Confused Rick",
  "Water Rick",
  "Hopeful Rick",
  "Agent Rick",
  "Gangsta Rick",
  "Wolf Pack Rick"
]
repeats = []

while len(repeats) != len(rickPictures):
  num = random.randrange(len(rickPictures))
  
  if not num in repeats:
    repeats.append(num)
    print rickPictures[num]
