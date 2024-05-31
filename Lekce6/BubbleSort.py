items = [1, 4, 2, 10, 4, 5, 6, 43]

def bubblesort(items): # n -> delka items (velikost vstupu)
    for j in range(len(items) - 1):
        for i in range(len(items) -1):
            #print(i)
            if items[i] < items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]

                #temp = items[i]    jiny způsob přehazování
                #items[i] = items[i + 1]
                #items[i + 1] = temp



#optimalizace
def bubblesort2(items): # n -> delka items (velikost vstupu)
    scrambled = True
    while scrambled:
        scrambled = False
        for i in range(len(items) -1):
            if items[i] < items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                scrambled = True

print(f"delka items: {len(items)}")
bubblesort(items)
print(items)

bubblesort2(items)
print(items)