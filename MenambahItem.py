import data

gadget_csv_modified = data.gadget
consumable_csv_modified = data.consumable

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

def tambah_item():
    new_item = []
    datas = []
    id = input("Masukan ID: ")
    if (not is_id_valid(id)):
        print("Gagal menambahkan item karena ID tidak valid.")
    else: 
        if (isGadgetOrConsumable(id) == "gadget"):
            datas = gadget_csv_modified
        else:
            datas = consumable_csv_modified
        if(is_id_available(id, datas) == True):
            print("Gagal menambahkan item karena ID sudah ada.")
        else:
            nama = input("Masukan Nama: ")
            deskripsi = input("Masukan Deskripsi: ")
            jumlah = int(input("Masukan Jumlah: "))
            rarity = input("Masukan Rarity: ")
            if (not is_rarity_valid(rarity)):
                print("Input rarity tidak valid!")
            else:
                if (isGadgetOrConsumable(id) == "gadget"):
                    tahun_ditemukan = int(input("Masukan tahun ditemukan: "))
                    new_item = [id,nama,deskripsi,jumlah,rarity,tahun_ditemukan]
                else:
                    new_item = [id,nama,deskripsi,jumlah,rarity]
                print("Item telah berhasil ditambahkan ke database.")
                if (isGadgetOrConsumable(id) == "gadget"):
                    gadget_csv_modified.append(new_item)
                else:
                    consumable_csv_modified.append(new_item)
tambah_item()
print(gadget_csv_modified)