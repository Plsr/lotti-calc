import random

nummer1 = random.randrange(1, 11)
nummer2 = random.randrange(1, 11)

ergebnis = input(f"{nummer1} + {nummer2} = ")

if int(ergebnis) == nummer1 + nummer2:
  print("✅ Richtig!")
else:
  print("❌ Falsch!")
