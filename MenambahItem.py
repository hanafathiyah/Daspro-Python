import data
from adding_function import is_id_available
from adding_function import is_id_valid
from adding_function import find_raw
from adding_function import is_rarity_valid
from adding_function import isGadgetOrConsumable
from adding_function import banyak_data

def tambah_item():
    new_item = []
    datas = []
    id = input("Masukan ID: ")
    if (not is_id_valid(id)):
        print("Gagal menambahkan item karena ID tidak valid.")
    else: 
        if (isGadgetOrConsumable(id) == "gadget"):
            datas = data.gadget
        else:
            datas = data.consumable
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
                    data.gadget.append(new_item)
                else:
                    data.consumable.append(new_item)