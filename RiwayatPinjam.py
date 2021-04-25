import data
from adding_function import sortTanggal
from adding_function import find_user_name_id
from adding_function import find_gadget_name_id
from LoadData import load_data
load_data("folder_isi")

# procedure melihat riwayat peminjaman gadget
def riwayatpinjam():
    datas = data.gadget_borrow_history
    f = "riwayatpinjam"
    datas_sort = sortTanggal(datas,f) # data yang telah terurut descending berdasarkan tahun disimpan dalam array datas_sort
    i = 0
    while (i < len(datas_sort)): # perulangan untuk mencetak data ke layar
        print("ID Peminjaman\t\t:", datas_sort[i][0])
        print("Nama Peminjam\t\t:", find_user_name_id(datas_sort[i][1])) # translasi id user menjadi nama user
        print("Nama Gadget\t\t:", find_gadget_name_id(datas_sort[i][2])) # translasi id gadget menjadi nama gadget
        print("Tanggal Peminjaman\t:", datas_sort[i][3])
        print("Jumlah\t\t\t:", datas_sort[i][4])
        print("")
        if ((i + 1) % 5 == 0): # apabila pengguna ingin mengeluarkan entry tambahan
            tambahan = input("Next >> Y/N: ")
            if tambahan == "N": # pengguna tidak ingin mengeluarkan entry tambahan
                break
            else: # pengguna ingin mengeluarkan entry tambahan
                print("")
        i += 1
        
riwayatpinjam()
