# import file, fungsi, dan prosedur
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

# procedure tambah_item
def tambah_item(): 
    new_item = []
    datas = []
    id = input("Masukan ID: ") # input id
    if (not is_id_valid(id)): # validasi id : id tidak valid
        print("Gagal menambahkan item karena ID tidak valid.")
    else: # validasi id : id valid
        if (isGadgetOrConsumable(id) == "gadget"): # mengecek jenis benda berdasarkan id
            datas = data.gadget
        else:
            datas = data.consumable
        if(is_id_available(id, datas) == True): # validasi ketersediaan id : id sudah tersedia
            print("Gagal menambahkan item karena ID sudah ada.")
        else: # validasi ketersediaan id : id belum tersedia
            nama = input("Masukan Nama: ") # input nama
            deskripsi = input("Masukan Deskripsi: ") # input deskripsi
            jumlah = input("Masukan Jumlah: ") # input jumlah
            if (not is_jumlah_valid(jumlah)): # validasi jumlah : jumlah tidak valid
                print("Input jumlah tidak valid!") 
            else: # validasi jumlah : jumlah valid
                rarity = input("Masukan Rarity: ") # input rarity
                if (not is_rarity_valid(rarity)): # validasi rarity : rarity valid
                    print("Input rarity tidak valid!")
                else: # validasi rarity : rarity tidak valid
                    if (isGadgetOrConsumable(id) == "consumable"):
                        new_item = [id,nama,deskripsi,jumlah,rarity]
                        data.consumable.append(new_item) # menambahkan item baru pada array consumable
                        print("Item telah berhasil ditambahkan ke database.")
                    else:
                        tahun_ditemukan = input("Masukan tahun ditemukan: ") # input tahun ditemukan
                        if (not is_tahun_valid(tahun_ditemukan)): # validasi tahun ditemukan : tahun tidak valid
                            print("Input tahun tidak valid!")
                        else: # validasi tahun ditemukan : tahun valid
                            new_item = [id,nama,deskripsi,jumlah,rarity,tahun_ditemukan]
                            data.gadget.append(new_item) # menambahkan item baru pada array gadget
                            print("Item telah berhasil ditambahkan ke database.")