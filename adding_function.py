def is_id_available(id,datas):
    i = 0
    available = False
    while i < banyak_data(datas) and available == False:
        if (datas[i][0] == id):
            available = True
        else:
            i += 1
    return available

def is_id_valid(id):
    valid = False
    if (id[0] == "G" or id[0] == "C"):
        valid = True
    return valid

def find_raw(id, datas):
    i = 0
    found = False
    while i < banyak_data(datas) and found == False:
        if (datas[i][0] == id):
            found = True
        else:
            i += 1
    return i

def is_rarity_valid(rarity):
    valid = False
    if (rarity == "C" or rarity == "B" or rarity == "A" or rarity == "S"):
        valid = True
    return valid
    
def isGadgetOrConsumable(id):
    if (id[0] == "G"):
        return "gadget"
    else:
        return "consumable"

def banyak_data(datas):
    cnt = 0
    for data in datas:
        cnt += 1
    return(cnt)
