# Dictionaries


l = ["adam", "eva"]


d = {"key": "value",
     "key2": 2,
     "name": "Adam",
     "key3": {"name":3},
     "key4": [1,2,3]}

player = {"name": "Adam",
          "attack": 4,
          "deffense": 2,
          "name": "test"}




print(d)
print(player["name"])
player["name"] = "EVA"
print(player)
player["friend"] = "Adam"
#print(player["age"])
print(player)
del player["friend"]
print(player)


print()
for item in player:
    print(item)
    print(player[item])



print()
for (k,v) in player.items():
    print(f"k: {k}, v: {v}")


print()
for i, (k,v) in enumerate(player.items()):
    print(f"i: {i+1}, k: {k}, v: {v}")


print()
for v in player.values():
    print(f"v: {v}")

print()
print(player.keys())

#player["age"] += 2
#player["age"] = player["age"] + 2


#print(player["age"])
print(player.get("age"))# is not None)
player.update([["pages", 700], ("online", False)])
print(player) 