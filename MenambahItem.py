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
from adding_function import isAdmin
from desain import tambahitem_header
from color import red, green

# load_data("folder_isi")

# prosedur menambah item
def tambah_item(): 
    tambahitem_header()
    if not isAdmin(): # validasi akses : akses tidak diizinkan
        print("Fungsi ini hanya dapat diakses oleh", red("Admin."))
    else: # validasi akses : akses diizinkan
        new_item = []
        datas = []
        id = input("Masukan ID: ") # input id
        if (not is_id_valid(id)): # validasi id : id tidak valid
            print(red("Gagal"), "menambahkan item karena", red("ID tidak valid."))
        else: # validasi id : id valid
            if (isGadgetOrConsumable(id) == "gadget"): # mengecek jenis benda berdasarkan id
                datas = data.gadget
            else:
                datas = data.consumable
            if(is_id_available(id, datas) == True): # validasi ketersediaan id : id sudah tersedia
                print(red("Gagal"), "menambahkan item karena", red("ID sudah ada."))
            else: # validasi ketersediaan id : id belum tersedia
                nama = input("Masukan Nama: ") # input nama
                deskripsi = input("Masukan Deskripsi: ") # input deskripsi
                jumlah = input("Masukan Jumlah: ") # input jumlah
                if (not is_jumlah_valid(jumlah)): # validasi jumlah : jumlah tidak valid
                    print("Input jumlah",red("tidak valid!")) 
                else: # validasi jumlah : jumlah valid
                    rarity = input("Masukan Rarity: ") # input rarity
                    if (not is_rarity_valid(rarity)): # validasi rarity : rarity tidak valid
                        print("Input rarity", red("tidak valid!"))
                    else: # validasi rarity : rarity valid
                        if (isGadgetOrConsumable(id) == "consumable"):
                            new_item = [id,nama,deskripsi,int(jumlah),rarity]
                            data.consumable.append(new_item) # menambahkan item baru pada array consumable
                            print("Item telah", green("berhasil"), "ditambahkan ke database.")
                        else:
                            tahun_ditemukan = input("Masukan tahun ditemukan: ") # input tahun ditemukan
                            if (not is_tahun_valid(tahun_ditemukan)): # validasi tahun ditemukan : tahun tidak valid
                                print("Input tahun", red("tidak valid!"))
                            else: # validasi tahun ditemukan : tahun valid
                                new_item = [id,nama,deskripsi,int(jumlah),rarity,tahun_ditemukan]
                                data.gadget.append(new_item) # menambahkan item baru pada array gadget
                                print("Item telah", green("berhasil"), "ditambahkan ke database.")