import data
from LoadData import load_data
from adding_function import is_id_available
from adding_function import is_id_valid
from adding_function import find_raw
from adding_function import is_rarity_valid
from adding_function import isGadgetOrConsumable
from adding_function import banyak_data
from adding_function import is_tanggal_valid
from adding_function import find_gadget_name_id
from adding_function import isUser


# Keperluan testing
# from Login import login
# load_data("folder_isi")

def pinjam():
    role_user = data.user_login[5]
    id_username = data.user_login[0]

    # Validasi role user 
    if (not isUser()) :
        return print("Fungsi ini hanya dapat diakses oleh user")

    datas = data.gadget
    id = input("Masukan ID: ")
     # Verifikasi ID
    if (not is_id_valid(id)): 
        print("Gagal menambah item karena ID tidak valid.") 
    elif(not is_id_available(id, datas)):
            print("Gagal menambah item karena ID tidak ada.")

    # Verifikasi apakah gadget sudah dipinjam atau belum
    datax = data.gadget_borrow_history
    j = 0 
    is_borrowed = False
    while j < banyak_data(datax) : 
        if id_username == datax[j][1] and id == datax[j][2]  and datax[j][5] == 'False' :
            print(f'Anda tercatat sudah meminjam gadget {find_gadget_name_id(datax[j][2])}')
            is_borrowed = True
            break
        else :
            j += 1
    
    if (is_id_valid(id) and is_id_available(id, datas) and is_borrowed == False) :
        tgl = input("Tanggal peminjaman: ")
        if (not is_tanggal_valid(tgl)) : 
            print("Tanggal peminjaman tidak valid !")
        else :
            jumlah = int(input("Jumlah peminjaman: "))
            if jumlah > datas[find_raw(id, datas)][3]:
                print(f"Item {datas[find_raw(id, datas)][1]} tidak berhasil dipinjam. Jumlah peminjaman terlalu banyak!")
            elif jumlah <= 0 : 
                print(f"Item {datas[find_raw(id, datas)][1]} tidak berhasil dipinjam. Jumlah peminjaman harus lebih besar dari 0")
            else :
                print(f"Item {datas[find_raw(id, datas)][1]} (x{jumlah}) telah berhasil dipinjam!")
                data.gadget[find_raw(id, datas)][3] -= jumlah
                is_returned = False

                # Pengambilan id_username
                id_username = data.user_login[0]

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
                new_peminjaman = [id_transaksi,id_username, id, tgl, jumlah, is_returned, jumlah]
                data.gadget_borrow_history.append(new_peminjaman)


# Keperluan testing
# login()
# pinjam()
