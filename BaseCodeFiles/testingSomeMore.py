from GameData import GameData

gm = GameData()
print(gm)
print(gm.getGameData())
hap, hunger, thirst, money, savings, time, items = gm.getGameData()

print(hap, hunger, thirst, money, savings, time, items)