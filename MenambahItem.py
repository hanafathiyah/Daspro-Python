import data
from LoadData import load_data
from adding_function import is_jumlah_valid
from adding_function import is_tahun_valid
from adding_function import is_id_available
from adding_function import is_id_valid
from adding_function import find_raw
from adding_function import is_rarity_valid
from adding_function import isGadgetOrConsumable
from adding_function import banyak_data
load_data("folder_isi")

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
            jumlah = input("Masukan Jumlah: ")
            if (not is_jumlah_valid(jumlah)):
                print("Input jumlah tidak valid!")
            else:
                rarity = input("Masukan Rarity: ")
                if (not is_rarity_valid(rarity)):
                    print("Input rarity tidak valid!")
                else:
                    if (isGadgetOrConsumable(id) == "consumable"):
                        new_item = [id,nama,deskripsi,jumlah,rarity]
                        data.consumable.append(new_item)
                        print("Item telah berhasil ditambahkan ke database.")
                    else:
                        tahun_ditemukan = input("Masukan tahun ditemukan: ")
                        if (not is_tahun_valid(tahun_ditemukan)):
                            print("Input tahun tidak valid!")
                        else:
                            new_item = [id,nama,deskripsi,jumlah,rarity,tahun_ditemukan]
                            data.gadget.append(new_item)
                            print("Item telah berhasil ditambahkan ke database.")