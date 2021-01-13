def change(amount):
    assert(amount>=8)
    if amount == 8 :
        return[3,5]
    if amount == 9:
        return[3,3,3]
    if amount == 10 :
        return[5,5]
    coins = change(amount - 3)
    coins.append(3)
    return coins
#print(change(16))
#%%
def change(amount):
    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5,5,5,5,5]
    if amount == 26 :
        return [7,7,7,5]
    if amount == 27 :
        return [5,5,5,5,7]
    if amount == 28 :
        return [7,7,7,7]
    coins = change(amount - 5)
    coins.append(5)
    return coins
print(change(99))
#%%