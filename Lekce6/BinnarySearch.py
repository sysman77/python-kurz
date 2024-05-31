def binnary_search(item, items, start, end):
    if start >= end:
        return False

    half = (start + end) // 2

    if half < 0 or half > len(items) - 1:
        return False
    
    if item == items[half]:
        return True

    elif item > items[half]:
        result = binnary_search(item, items, half, end)
        return result

    else:
        return binnary_search(item, items, start, half)


items = [1, 4, 5, 6, 8, 10]
print(items)
print(binnary_search, 4, items, 0, len(items))



"""
def binnary_search(item, items, start, end): # 5 6
    if start >= end:
        return False

    half = (start + end) // 2

    if half < 0 or half > len(items) - 1:
        return False
    
    if item == items[half]:
        return True

    elif item > items[half]:
        result = binnary_search(item, items, half, end)
        return result

    else:
        return binnary_search(item, items, start, half)

    
    
print(items2)
print(binnary_search(7, items2, 0, len(items))) 

"""
