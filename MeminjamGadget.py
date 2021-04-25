import data
from LoadData import load_data
from adding_function import is_id_available
from adding_function import is_id_valid
from adding_function import find_raw
from adding_function import is_rarity_valid
from adding_function import isGadgetOrConsumable
from adding_function import banyak_data

# Mengambil username
import Login
from Login import user_username


load_data("folder_isi")
def pinjam():

    datas = data.gadget
    id = input("Masukan ID: ")
     # Verifikasi ID
    if (not is_id_valid(id)): 
        print("Gagal menambah item karena ID tidak valid.") 
    elif(not is_id_available(id, datas)):
            print("Gagal menambah item karena ID tidak ada.")
    else : 
        tgl = input("Tanggal peminjaman: ")
        jumlah = int(input("Jumlah peminjaman: "))
        
        if jumlah > datas[find_raw(id, datas)][3]:
            print(f"Item {datas[find_raw(id, datas)][1]} tidak berhasil dipinjam. Jumlah peminjaman terlalu banyak!")
        if jumlah <= 0 : 
            print(f"Item {datas[find_raw(id, datas)][1]} tidak berhasil dipinjam. Jumlah peminjaman harus lebih besar dari 0")
        print(f"Item {datas[find_raw(id, datas)][1]} (x{jumlah}) berhasil dipinjam!")
        data.gadget[find_raw(id, datas)][3] -= jumlah
        is_returned = False

        # Pengambilan id_username

    

        # Pembuatan id transaksi otomatis
        id_transaksi = 1
        data_peminjaman = data.gadget_borrow_history
        i = 0
        available = False
        while i < banyak_data(data_peminjaman) and available == False:
            if (datas[i][0] != id_transaksi) and available == True :
                available = True
            else:
                i += 1
                id_transaksi += 1

        # Penambahan pada array
        new_peminjaman = [id_transaksi,id_username, id, tgl, jumlah, is_returned]
        data.gadget_borrow_history.append(new_peminjaman)
pinjam()
