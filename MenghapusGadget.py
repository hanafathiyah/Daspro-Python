import data
from LoadData import load_data
from adding_function import is_id_available
from adding_function import is_id_valid
from adding_function import find_raw
from adding_function import is_rarity_valid
from adding_function import isGadgetOrConsumable
from adding_function import banyak_data

load_data('folder_isi')

def mengapus_gadget() :
    datas = data.gadget
    id = input("Masukan ID: ")
    
    # Verifikasi ID
    if (not is_id_valid(id)): 
        print("Gagal menambah item karena ID tidak valid.")
    else: 
        if(not is_id_available(id, datas)):
            print("Gagal menambah item karena ID tidak ada.")

    if (is_id_valid(id)) and (is_id_available(id, datas)) : 
        Pilihan = input("Apakah yakin anda mau menghapus gadget tersebut (Y/N)? ")
        if Pilihan == 'Y' :
            i = 0
            while i < banyak_data(datas) :
                if (datas[i][0] == id):
                    datas.pop(i)    # Menghapus Data
                else:
                    i += 1
        elif Pilihan != 'N' : 
            print("Pilihan tidak valid")
        