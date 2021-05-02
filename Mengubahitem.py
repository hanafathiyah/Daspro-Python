import data
from LoadData import load_data
from adding_function import is_id_available
from adding_function import is_id_valid
from adding_function import find_raw
from adding_function import is_rarity_valid
from adding_function import isGadgetOrConsumable
from adding_function import banyak_data
from adding_function import isAdmin
from desain import ubahjumlah_header
from color import red, green

# load_data("folder_isi")
def mengubah_jumlah_item() :
    ubahjumlah_header()

    # Validasi role user 
    if (not isAdmin()) :
        return print("Fungsi ini hanya dapat diakses oleh", red("admin"))
    
    id = input("Masukan ID: ")
    if (isGadgetOrConsumable(id) == "gadget"): # Data yang di Load Gadget
        datas = data.gadget
    else: # Data yang di Load Consumable
        datas = data.consumable 
    
    # Verifikasi ID
    if (not is_id_valid(id)): 
        print(red("Gagal"), "mengubah jumlah item karena", red("ID tidak valid."))
    else: 
        if(not is_id_available(id, datas)):
            print(red("Gagal"),"mengubah jumlah item karena", red("ID tidak ada."))

    if (is_id_valid(id)) and (is_id_available(id, datas)) : 
        jumlah_diganti = int(input("Masukkan jumlah : ")) # Input jumlah yang akan diubah
        if jumlah_diganti < 0 : # Apabila akan membuang
            if (jumlah_diganti * -1) > datas[find_raw(id, datas)][3]: # Apabila jumlah yang dibuang melebihi stok
                jumlah_diganti = jumlah_diganti * -1
                print(f"{jumlah_diganti} {datas[find_raw(id, datas)][1]}", red("tidak berhasil"),f"dibuang. Stok sekarang : {datas[find_raw(id, datas)][3]} (<{jumlah_diganti})")
            else :
                print(f"{(jumlah_diganti) * -1} {datas[find_raw(id, datas)][1]}",green("berhasil"), f"dibuang. Stok sekarang : {(datas[find_raw(id, datas)][3]) + jumlah_diganti}")
        else : 
            print(f"{jumlah_diganti} {datas[find_raw(id, datas)][1]}",green("berhasil"), f"ditambahkan. Stok sekarang : {(datas[find_raw(id, datas)][3]) + jumlah_diganti}")
        if (isGadgetOrConsumable(id) == "gadget"):
            data.gadget[find_raw(id, datas)][3] += jumlah_diganti 
        else:
            data.consumable[find_raw(id, datas)][3] += jumlah_diganti

