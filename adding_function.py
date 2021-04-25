def is_id_available(id,datas): # mengecek ketersediaan id dalam database
    i = 0 # inisialisasi
    available = False # inisialisasi
    while i < banyak_data(datas) and available == False:
        if (datas[i][0] == id): # id tersedia
            available = True
        else: 
            i += 1
    return available

def is_id_valid(id): # validasi id
    valid = False # inisialisasi
    if (id[0] == "G" or id[0] == "C"): # id valid
        valid = True
    return valid

def find_raw(id, datas): # mencari letak id (dalam baris)
    i = 0 # inisialisasi
    found = False # inisialisasi
    while i < banyak_data(datas) and found == False: 
        if (datas[i][0] == id): # id berhasil ditemukan
            found = True
        else:
            i += 1
    return i

def is_rarity_valid(rarity): # validasi rarity
    valid = False # inisialisasi
    if (rarity == "C" or rarity == "B" or rarity == "A" or rarity == "S"): # rarity valid
        valid = True
    return valid

def is_tahun_valid(tahun): # validasi tahun
    if tahun.isalnum: # tahun merupakan angka
        if int(tahun) <= 0: # tahun tidak valid
            return False
        else: # tahun valid
            return True
    else: # tahun bukan merupakan angka
        return False

def is_jumlah_valid(jumlah): # validasi jumlah
    if jumlah.isalnum: # jumlah merupakan angka
        if int(jumlah) <= 0: # jumlah tidak valid
            return False
        else: # jumlah valid
            return True
    else: # jumlah bukan merupakan angka
        return False
    
def isGadgetOrConsumable(id): # mengecek apakah item tersebut gadget atau consumable
    if (id[0] == "G"): # item adalah gadget
        return "gadget"
    else: # item adalah consumable
        return "consumable"

def banyak_data(datas): # menghitung banyak data
    cnt = 0 # inisialisasi
    for data in datas:
        cnt += 1
    return(cnt) # banyak data
