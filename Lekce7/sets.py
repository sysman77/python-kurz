# SETS - množiny

s = {1,2,3,4}
print(s)

for item in s:
    print(item)


w = set(["word","hello"])

print(w)

w.add("add")

print(w)

w.update(["update", "update2"])
print(w)

w.remove("add")
print(w)

w.discard("update")
print(w)

print(min(w))

# https://realpython.com/python-sets/
